import os
import subprocess, sys
import json

if __name__ == '__main__':

	IsFromAPKMirror = True
	Category = 'TOOLS'

	if IsFromAPKMirror:


		#python ./aptoide.py 'EDUCATION' 'QuizLet'

		#EDUCATIO
		#Apps = ['QuizLet', 'RosettaStone', 'Lumosity']
		#Urls = ['quizlet','languages','lumosity']

		#PRODUCTIVITY
	#	Apps = [
	#		'adobe-acrobat-reader', 'camscanner', 'dropbox', 
	#		'evernote', 'super-file-manager', 'fleksy-legacy', 
	#		'gboard-the-google-keyboard', 'google-inc-calendar','docs', 
	#		'google-drive', 'keep', 'google-talkback',
	#		'google-sheets','slides','lastpass-authenticator',
	#		'mega','cortana','microsoft-excel',
	#		'outlook','office-mobile','microsoft-powerpoint',
	#		'microsoft-corporation-to-do','microsoft-word','nytimes-latest-news',
	#		'pokemon-tv','samsung-notes','starbucks',
	#		'com-teamviewer-teamviewer','comcast-interactive-media-tv','es-file-explorer',
	#		]
		Apps = [
			'avast-cleanup','bittorrent','snaptube',
			'brave','calculator','ccleaner',
			'kika-keyboard','google-inc-clock','google-opinion-rewards',
			'google-translate','google-inc-earth','',
			'kernel-booster','lookout-security-antivirus','microsoft-bing',
			'opera-mini-web-browser','network-signal-guru','network-signal-info',
			'peel-remote','remote-control-collection','root-checker-basic',
			'shareit','android-deskclock','teamviewer',
			'titanium-backup','tv-vodafone','vrem-software-development-wifi-analyzer',
			'wifi-analyzer','home','fire-tv',
			]
		#Urls = ['adobe-acrobat-reader','camscanner','lumosity']
		
		i = 0
		for app in Apps:

			Command = "python ./aptoide.py '" + Category + "' '" + app + "' 'https://" + app + ".en.aptoide.com/versions'" 
			print("Command " + Command)
			os.system(Command)

	else:

		Apps =  [
				'aida','App Lock','Bill',
				'Box','Boxer','BusyBox X',
				'BusyBox Stephen','Facebook Ads','File Commander',
				'FX File','Google My','Google Primer',
				'Hangouts Meet','LinkedIn Job','Microsoft Authenticator',
				'Microsoft Power','Microsoft Remote','My Verizon',
				'My Business','OfficeSuite','Paypa Here',
				'pulse','Recharge Bill','SamsungBilling',
				'SINC','Skype for','Slack',
				'slacker','TotalCommander','Web',
				'wire','word to','workplace by',
				'workplace chat'
				]


		#Category = 'TOOLS'
		#Apps = [
		#	'Titanium Backup','SuperSU', 'Network Signal Guru',
		#	 'Root Checker', 'WiFiAnalyzer (open-source)', 'XPosed Installer', 
		#	 'FlashFire', 'Lumen', ' SpeedTest Ookla', 'Kernel'

		 #]
		
		#Apps = ['yandex Browser', 'Canvas', 'Kids Drawing', 'Samsung pen up', 'sony sketch','tv time Toze', 'Khan Academy', 'Notes blackberry','Ampere', 'Pocket: Save', 'Google Art & Culture']
		# Bussiness stitcher', 'aliexpress',
		
		for app in Apps:

			Command = "python ./GetCategoryAppsList.py '" + Category + "' 0 '" + app + "'"
			print("Command " + Command)
			os.system(Command)
			

	for app in Apps:
		Command = "python ./SummarizeApks.py '" + Category + "' '" + app +"'"
		print("Command " + Command)
		os.system(Command)