import time
jdbcProv = "Oracle JDBC Driver"
nodeName = AdminControl.getNode()
srvrInfo=AdminConfig.list('Server') 
srvr=AdminConfig.showAttribute(srvrInfo, 'name')
jndiDS = "jdbc/ECC"
dbasename = "database location"
cell = AdminControl.getCell()


def j2cAuth(j2cAlias, j2cUserid,j2cPassword):
	security = AdminConfig.getid('/Cell:'+cell+'/Security:/')
	print security
	print AdminConfig.required('JAASAuthData')
	alias = ['alias', j2cAlias]
	userid = ['userId', j2cUserid]
	password = ['password', j2cPassword]
	jaasAttrs = [alias, userid, password]
	print alias
	print userid
	print AdminConfig.create('JAASAuthData', security, jaasAttrs)
	AdminConfig.save()
    	print "***************j2c authentication created****************"

#function to create jdbc provider
def createProvider():

	#if the JDBC Provider exists, then don't do anything
    	prov = AdminControl.completeObjectName("name=" + jdbcProv + ",type=JDBCProvider,Server=" + srvr + ",node=" + nodeName + ",*")
	if len(prov) > 0:
		print "\n***** The JDBC Provider with name: " + jdbcProv + " already exists. So another will not be created"
		return  
	#endif

	provName=['name',jdbcProv]
	impClass=['implementationClassName','oracle.jdbc.pool.OracleConnectionPoolDataSource'] 
   	jdbcAttrs=[]
    	jdbcAttrs.append(provName)
    	jdbcAttrs.append(impClass)

	# Create the JDBC Provider using the Oracle JDBC Driver template
    	tmplName = 'Oracle JDBC Driver'
    	templates = AdminConfig.listTemplates("JDBCProvider", tmplName).split(lineSeparator)
   	tmpl = templates[0]
   	
	serverId = AdminConfig.getid("/Node:" + nodeName + "/Server:" + srvr + "/")

    	AdminConfig.createUsingTemplate("JDBCProvider",serverId,jdbcAttrs,tmpl)
    	AdminConfig.save()
        print jdbcProv + " has been created using the template. Config saved .."
# function to create the datasource
def createDS(dataSourceName, jndi):
	
	#if the DataSource exists, then don't do anything
   	dsId = AdminConfig.getid("/JDBCProvider:" + jdbcProv + "/DataSource:" + dataSourceName + "/")
   	if len(dsId) > 0:
		print "\n***** The DataSource with name: " + dataSourceName + " already exists. So another will not be created"
		return 
	#endif

	dsname=['name',dataSourceName]
	jndiName=['jndiName',jndi]
	description=['description','SIB DataSource']	
	dsHelperClassname=['datasourceHelperClassname','com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper']
    	dsAttrs=[]
    	dsAttrs.append(dsname)
    	dsAttrs.append(jndiName)
    	dsAttrs.append(description)
    	dsAttrs.append(dsHelperClassname)
    	
	provId = AdminConfig.getid("/Node:" + nodeName + "/Server:" + srvr + "/JDBCProvider:" + jdbcProv + "/")	
	AdminConfig.required('DataSource')
    	AdminConfig.create('DataSource',provId,dsAttrs)
	AdminConfig.save()
	print "Done creating the DS. Config saved .."
	
	#modifyDS() 
	
	print "\n***** Datasource created******"

#enddef        
# function to modify the data source
def modifyDS():
	
	#modify DS to add the ResourcePropertySet, esp the DatabaseName (location)
   	dsId = AdminConfig.getid("/JDBCProvider:" + jdbcProv + "/DataSource:" + dataSourceName + "/")
   	dbnameAttrs = [["name", "databaseName"], ["value", dbasename], ["type", "java.lang.String"], ["description", "This is a required property"]]
   	descrAttrs = [["name", "description"], ["value", ""], ["type", "java.lang.String"]] 
   	passwordAttrs = [["name", "password"], ["value", ""], ["type", "java.lang.String"]]
	loginTimeOutAttrs = [["name", "loginTimeout"], ["value", 0], ["type", "java.lang.Integer"]]
   	propset = []
   	propset.append(dbnameAttrs)
   	propset.append(descrAttrs)
   	propset.append(passwordAttrs)
   	propset.append(loginTimeOutAttrs) 
   	pSet = ["propertySet", [["resourceProperties", propset]]]
   	attrs = [pSet]
   	AdminConfig.modify(dsId, attrs)
	AdminConfig.save()
	print "Done modifying the DS. Config Saved .."
   	
#enddef


def installWar(warLoc, appName, contextUri):
	node = AdminConfig.getid('/Node:node111/')
	print node
	print  AdminControl.queryNames('WebSphere:type=Server,*')
	print " Cell name is --> "+ cell
	cellName=AdminControl.getCell()
	print cellName
	nodeName=AdminControl.getNode()
	print " nodeName is --> "+ nodeName
	appManager=AdminControl.queryNames('cell='+cellName+',node=node111,type=ApplicationManager,process=WebSphere_Portal,*')
	print appManager
	application = AdminConfig.getid("/Deployment:"+appName+"/")
	len(application)
	app = len(application)
	if app:
	   print "Application wtih the same name already exists"
	   print "Terminating..."
	   #AdminApp.uninstall('NCHL')
	   #AdminConfig.save()
	else:	
	   print "installing war ...."
	   print AdminApp.install(warLoc,['-appname', appName ,'-target', 'default',' -usedefaultbindings','-defaultbinding.virtual.host','default_host','-contextroot',contextUri])
	   print "Application installed"
	   AdminConfig.save()
	   time.sleep(30)
	   AdminControl.invoke(appManager , 'startApplication',appName)
	   print "The script is completed." 


#j2cAuth('SIB_ECC','SIB_ECC','SIB_ECC')
#j2cAuth('sib_sec41','sib_sec41','sib_sec41')
#createProvider()
#createDS('SIB_ECC','jdbc/ECC')
#createDS('sib_sec41','jdbc/SEC')
installWar('/home/was/corporate-shell.war','corporate-shell','/corporate-shell')
  

    



