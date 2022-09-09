# import project libraries.
import wx
import speedtest
import requests
import threading
import ctypes
import pyperclip


try:
	speed = speedtest.Speedtest()
except:
	pass


# Create dialog window To ViewInfo
class ViewInfoDialog(wx.Dialog):
	def __init__(self, parent, service, ip=None):
		wx.Dialog.__init__(self, parent, title='View Info', size=(300, 400))
		#make window in center.
		self.Center()
		self.service = service
		self.ip = ip



		# Creating panel
		Panel = wx.Panel(self)

		# Create RichEdit to View Info
		self.title = wx.StaticText(Panel, -1, "Please wait.", pos=(10,10), size=(380,30))
		self.ViewInfo = wx.TextCtrl(Panel, -1, pos=(10,40), size=(270,250), style=wx.TE_RICH2+wx.TE_MULTILINE+wx.TE_READONLY)
		self.ThreadLoadInfo = thread(target=self.LoadInfo, daemon=True)
		self.ThreadLoadInfo.start()


		# Creating Buttons
		self.CopyInfo = wx.Button(Panel, -1, "Copy Info", pos=(10,310), size=(60,30))
		self.Close = wx.Button(Panel, wx.ID_CANCEL, "Close", pos=(200,310), size=(60,30))


		# events for buttons
		self.Close.Bind(wx.EVT_BUTTON, self.OnClose)
		self.CopyInfo.Bind(wx.EVT_BUTTON, self.OnCopyInfo)

		# Show Main window
		self.Show()

	#creating function to load the information
	def LoadInfo(self):
		#set the best server in case test download or upload or ping.
		if self.service in ("download", "upload", "download and upload", "ping"):
			speed.get_best_server()

		#getting speed download and display it.
		if self.service == "download":
			DownloadSpeed = round(speed.download()/1000000, 3)
			self.ViewInfo.Value = """Your speed test has completed.
your download speed is {}Mbps.
""".format(DownloadSpeed)

		#getting speed upload and display it.
		elif self.service == "upload":
			UploadSpeed = round(speed.upload()/1000000, 3)
			self.ViewInfo.Value = """Your speed test has completed.
your upload speed is {}Mbps.
""".format(UploadSpeed)

		#geting speed download and upload and display it.
		elif self.service == "download and upload":
			DownloadSpeed = round(speed.download()/1000000, 3)
			UploadSpeed = round(speed.upload()/1000000, 3)
			self.ViewInfo.Value = """Your speed test has completed.
your download speed is {}Mbps,
youre upload speed is {}Mbps.
""".format(DownloadSpeed, UploadSpeed)

	#getting pingand display it.
		elif self.service == "ping":
			ping = round(speed.results.ping, 1)
			self.ViewInfo.Value = """Your speed test has completed.
your ping is {}ms
""".format(ping)

		#getting current IP and display it.
		elif self.service == "get ip":
			self.ViewInfo.Value = "Your IP is {}.".format(get_ip())

		#getting information of current IP and display it.
		elif self.service == "ip info":
			ip = get_ip()
			try:
				info = get_ip_information(ip)
			except:
				info = get_location(ip)
			self.ViewInfo.Value = """ information has loaded.
IP: {}
country: {}.
country code: {}
city: {}
region: {}
""".format(info["ip"], info["country"], info["countryCode"], info["city"], info["region"])

		#getting information of external IP and display it.
		elif self.service == "get external IP Info":
			ip = self.ip
			try:
				info = get_ip_information(ip)
			except:
				info = get_location(ip)
			self.ViewInfo.Value = """ information has loaded.
IP: {}
country: {}.
country code: {}
city: {}
region: {}
""".format(info["ip"], info["country"], info["countryCode"], info["city"], info["region"])

		#After loading, the title will be set to information.
		self.title.SetLabel("information")

	#copy the information.
	def OnCopyInfo(self, ev):
		pyperclip.copy(self.ViewInfo.Value)

	#close the dialog
	def OnClose(self, ev):
		self.ThreadLoadInfo.stop()
		self.Destroy()

#end of class


#creating custom thread to able me to stop it.
class thread(threading.Thread):

	def get_id(self):
		# returns id of the respective thread
		if hasattr(self, '_thread_id'):
			return self._thread_id
		for id, thread in threading._active.items():
			if thread is self:
				return id
  
	def stop(self):
		self._is_stopped = True
		self.thread_id = self.get_id()
		self.res = ctypes.pythonapi.PyThreadState_SetAsyncExc(self.thread_id, ctypes.py_object(SystemExit))
		if self.res > 1:
			ctypes.pythonapi.PyThreadState_SetAsyncExc(self.thread_id, 0)

	def is_stopped(self):
		return self._is_stopped

	#end of class.


#creating function to get current IP.
def get_ip():
	response = requests.get('https://api64.ipify.org?format=json').json()
	return response["ip"]

#creating function to get IP information.
def get_location(ip):
	ip_address = ip
	response = requests.get(f"https://ipapi.co/{ip_address}/json/").json()
	location_data = {
	"ip": ip_address,
	"country": response.get("country_name"),
	"countryCode": response.get("country_code"),
	"city": response.get("city"),
	"region": response.get("region")
	}
	return location_data

#creating Additional function to get IP information.
def get_ip_information(ip):
	response = requests.get(f'http://ip-api.com/json/{ip}').json()
	location_data = {
	"ip": response.get("query"),
	"country": response.get("country"),
	"countryCode": response.get("countryCode"),
	"city": response.get("city"),
	"region": response.get("regionName")
	}
	return location_data

