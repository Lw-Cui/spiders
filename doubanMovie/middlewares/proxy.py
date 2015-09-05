import random
import base64

class MyProxyMiddleware(object):
	def process_request(self, request, spider):
		proxy = random.choice(self.proxy_list)
		#print "********Current Proxy IP:%s************" % proxy['ip_port']
		request.meta['proxy'] = "http://%s" % proxy['ip_port']

	proxy_list = [
	  {'ip_port': '124.240.187.77:80', 'user_pass': ''},
	  {'ip_port': '223.19.230.181:80', 'user_pass': ''},
	  {'ip_port': '61.235.249.222:80', 'user_pass': ''},
	  {'ip_port': '222.39.64.13:8118', 'user_pass': ''},
	  {'ip_port': '58.96.182.48:8090', 'user_pass': ''},
	  {'ip_port': '221.208.194.108:80', 'user_pass': ''},
	  {'ip_port': '183.178.98.88:8080', 'user_pass': ''},
	  {'ip_port': '121.199.69.234:8088', 'user_pass': ''},
	]
	