#python3.9
# import project libraries.
import wx
import speedtest
import requests
import webbrowser
from ViewInfo import *

# Create app with wx.
app= wx.App()

# Create main window with wx.
class SpeedTest(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title = 'Internet Speed Test', size=(550, 350))

		#make window in center.
		self.Center()

		#make window Minimum size.
		self.Maximize(False)
		self.EnableMaximizeButton(False)


		# Creating panel
		Panel = wx.Panel(self)

		# Creating Buttons
		self.UploadSpeed = wx.Button(Panel, -1, "UploadSpeed", pos=(350,40), size=(100,30))
		self.DownloadSpeed = wx.Button(Panel, -1, "DownloadSpeed", pos=(100,40), size=(100,30))
		self.BothDownloadAndUpload = wx.Button(Panel, -1, "BothDownloadAndUpload", pos=(180,90), size=(160,30))
		self.PingInfo = wx.Button(Panel, -1, "PingInfo", pos=(350,120), size=(100,30))
		self.IpInfo = wx.Button(Panel, -1, "IpInfo", pos=(70,120), size=(100,30))
		self.Help = wx.Button(Panel, -1, "Help", pos=(20,250), size=(60,30))
		self.Close = wx.Button(Panel, -1, "Close", pos=(450,250), size=(60,30))


		# Show Main window
		self.Show()

		# events for buttons
		self.IpInfo.Bind(wx.EVT_BUTTON, self.OnIpInfo)
		self.Help.Bind(wx.EVT_BUTTON, self.OnHelpMenu)
		self.Close.Bind(wx.EVT_BUTTON, self.OnCloseProgram)
		self.UploadSpeed.Bind(wx.EVT_BUTTON, self.OnUploadSpeed)
		self.DownloadSpeed.Bind(wx.EVT_BUTTON, self.OnDownloadSpeed)
		self.BothDownloadAndUpload.Bind(wx.EVT_BUTTON, self.OnBothDownloadAndUpload)
		self.PingInfo.Bind(wx.EVT_BUTTON, self.OnPingInfo)

	# Functions
	#Get Upload Speed Function
	def OnUploadSpeed(self, event):
		ViewInfoDialog(self, "upload")

	#Get Download Speed Function
	def OnDownloadSpeed(self, eve):
		ViewInfoDialog(self, "download")

	#Get Upload And Download Speed Function
	def OnBothDownloadAndUpload(self, event):
		ViewInfoDialog(self, "download and upload")

	#Get Ping Info  Speed Function
	def OnPingInfo(self, event):
		ViewInfoDialog(self, "ping")

	# IP Info Function
	def OnIpInfo(self, event):
		IPMenu = wx.Menu()
		GetMyIPItem = IPMenu.Append(-1, "Get My IP")
		GetMyIPInfoItem = IPMenu.Append(-1, "Get My IP Info")
		GetExternalIPInfoItem = IPMenu.Append(-1, "Get external IP Info")
		self.Bind(wx.EVT_MENU, self.OnGetMyIP, GetMyIPItem)
		self.Bind(wx.EVT_MENU, self.OnGetMyIPInfo, GetMyIPInfoItem)
		self.Bind(wx.EVT_MENU, self.OnGetExternalIPInfo, GetExternalIPInfoItem)
		self.PopupMenu(IPMenu)

	# IPInfo Menu Item Functions
	def OnGetMyIP(self, event):
		ViewInfoDialog(self, "get ip")

	def OnGetMyIPInfo(self, event):
		ViewInfoDialog(self, "ip info")

	def OnGetExternalIPInfo(self, event):
		ip = wx.GetTextFromUser("Input the external IP", "external IP")
		if ip:
			ViewInfoDialog(self, "get external IP Info", ip)

	# HelpMenu Functions
	def OnHelpMenu(self, event):
		HelpMenu = wx.Menu()
		HelpItem = HelpMenu.Append(-1, "Help")
		WebSiteItem = HelpMenu.Append(-1, "Visit WebSite")
		AboutItem = HelpMenu.Append(-1, "about")
		self.Bind(wx.EVT_MENU, self.OnHelp, HelpItem)
		self.Bind(wx.EVT_MENU, self.OnWebSite, WebSiteItem)
		self.Bind(wx.EVT_MENU, self.OnAbout, AboutItem)
		self.PopupMenu(HelpMenu)

	# Help Menu Item Functions
	def OnHelp(self, event):
		pass
	def OnWebSite(self, event):
		webbrowser.open_new('https://t.me/A2zTecChannel')
	def OnAbout(self, event):
		wx.MessageBox('With this tool, you can check your internet speed. Where you can know the download speed, upload speed and ping rate. You can also find out your IP address, and find out all the information about any IP that you type into the tool.', 'About Tool')


	# CloseProgram
	def OnCloseProgram(self, event):
		wx.Exit()

SpeedTest()
app.MainLoop()    