#from lib.pytube import YouTube
from lib.dewa import cari
from lib.anime import *
from lib.brainly import *
from lib.manga import *
from lib.resize import *
from lib.search import *
from lib.nulis import *
from urllib.parse import *
from flask import *
#from werkzeug.utils import *
from bs4 import BeautifulSoup as bs
from requests import get, post
import os, math, json, random, re, html_text, pytesseract, base64, time, smtplib

ua_ig = 'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)'

app = Flask(__name__)
apiKey = 'O8mUD3YrHIy9KM1fMRjamw8eg'
apiKey_ocr = '09731daace88957'
app.config['MEDIA'] = 'tts'
app.secret_key = b'BB,^z\x90\x88?\xcf\xbb'
#ALLOWED_EXTENSION = set(['png', 'jpeg', 'jpg'])
#app.config['Layer_Folder'] = 'layer'

def convert_size(size_bytes):
	if size_bytes == 0:
		return '0B'
	size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return '%s %s' % (s, size_name[i])

#def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/tts/<path:filename>', methods=['GET','POST'])
def sendTts(filename):
	return send_from_directory(app.config['MEDIA'], filename, as_attachment=True)

@app.route('/api/layer', methods=['GET','POST'])
def layer():
	if request.args.get('base64image'):
		try:
			open('piw.jpg','w').write(request.args.get('base64image'))
			os.system('base64 -i -d piw.jpg > paw.jpg')
			hehe = resizeTo('paw.jpg')
			huhu = layer(hehe, 'black')
			os.system('base64 result.jpg > pow.jpg')
			return {
			    'restapi' :  'ferdiz-afk',
				'status'  : 200,
				'result'  : '`data:image/jpg;base64,%s`' % open('pow.jpg').read()
			}
		except Exception as e:
			print(e)
			#os.remove('piw.jpg')
			return {
				'status': False,
				'error': '[!] Invalid base64 image!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter base64image'
		}


@app.route('/api/spamgmail', methods=['GET','POST'])
def spamgimel():
    if request.args.get('target'):
        if request.args.get('jum'):
            abece = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            target_imel = request.args.get('target')
            jumlah = int(request.args.get('jum'))
            if jumlah > 10:
                return {
                    'status': False,
                    'msg': '[!] Max 10 tod!'
                }
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('spamz.barbar@gmail.com', 'Barbar05')
                hasil = ''
                for i in range(jumlah):
                    mess = ''.join(random.choice(abece) for _ in range(4))
                    msg = f'From: {random.randint(1, 100)}<Hacker>\nSubject: Anonymous ~ Hacker\n{mess}'
                    server.sendmail('spamz.barbar@gmail.com', target_imel, msg)
                    hasil += '[!] Sukses\n'
                server.quit()
                return {
                    'status': 200,
                    'logs': hasil
                }
            except Exception as e:
                print(e)
                hasil = '[!] Gagal'
                return {
                    'status': False,
                    'logs': hasil
                }
        else:
            return {
                'status': False,
                'msg': 'Masukkan parameter jum'
            }
    else:
        return {
            'status': False,
            'msg': 'Masukkan parameter target'
        }

@app.route('/api/halah', methods=['GET','POST'])
def halah():
	if request.args.get('text'):
		text = str(request.args.get('text'))
		kantal = text.replace('a', 'a').replace('A', 'A').replace('u', 'a').replace('U', 'A').replace('e', 'a').replace('E', 'A').replace('o', 'a').replace('O', 'A')
		return { 'status': 200, 'result': kantal }
	else:
		return { 'status': False, 'pesan': 'Masukkan parameter text'}
		
		
@app.route('/api/hilih', methods=['GET','POST'])
def hilih():
	if request.args.get('text'):
		text = str(request.args.get('text'))
		kintil = text.replace('a', 'i').replace('A', 'I').replace('u', 'i').replace('U', 'I').replace('e', 'i').replace('E', 'I').replace('o', 'i').replace('O', 'I')
		return { 'status': 200, 'result': kintil }
	else:
		return { 'status': False, 'pesan': 'Masukkan parameter text'}
		
		
@app.route('/api/huluh', methods=['GET','POST'])
def huluh():
	if request.args.get('text'):
		text = str(request.args.get('text'))
		kuntul = text.replace('a', 'u').replace('A', 'U').replace('u', 'u').replace('U', 'U').replace('e', 'u').replace('E', 'U').replace('o', 'u').replace('O', 'U')
		return { 'status': 200, 'result': kuntul }
	else:
		return { 'status': False, 'pesan': 'Masukkan parameter text'}

@app.route('/api/ytv', methods=['GET','POST'])
def ytv():
	if request.args.get('url'):
		try:
			url = request.args.get('url').replace('[','').replace(']','')
			ytv = post('https://www.y2mate.com/mates/en60/analyze/ajax',data={'url':url,'q_auto':'0','ajax':'1'}).json()
			yaha = bs(ytv['result'], 'html.parser').findAll('td')
			filesize = yaha[len(yaha)-23].text
			id = re.findall('var k__id = "(.*?)"', ytv['result'])
			thumb = bs(ytv['result'], 'html.parser').find('img')['src']
			title = bs(ytv['result'], 'html.parser').find('b').text
			dl_link = bs(post('https://www.y2mate.com/mates/en60/convert',data={'type':url.split('/')[2],'_id':id[0],'v_id':url.split('/')[3],'ajax':'1','token':'','ftype':'mp4','fquality':'360p'}).json()['result'],'html.parser').find('a')['href']
			return {
				'status': 200,
				'restapi' : 'ferdiz-afk',
				'title': title,
				'thumb': thumb,
				'result': dl_link,
				'resolution': '360p',
				'filesize': filesize,
				'ext': 'mp4'
			}
		except Exception as e:
			print('Error : %s ' % e)
			return {
				'status': False,
				'error': '[❗] Terjadi kesalahan, mungkin link yang anda kirim tidak valid!'
			}
	else:
		return {
			'status': False,
			'msg': 'Masukkan parameter url'
		}

@app.route('/api/yta', methods=['GET','POST'])
def yta():
	if request.args.get('url'):
		try:
			url = request.args.get('url').replace('[','').replace(']','')
			yta = post('https://www.y2mate.com/mates/en60/analyze/ajax',data={'url':url,'q_auto':'0','ajax':'1'}).json()
			yaha = bs(yta['result'], 'html.parser').findAll('td')
			filesize = yaha[len(yaha)-10].text
			id = re.findall('var k__id = "(.*?)"', yta['result'])
			thumb = bs(yta['result'], 'html.parser').find('img')['src']
			title = bs(yta['result'], 'html.parser').find('b').text
			dl_link = bs(post('https://www.y2mate.com/mates/en60/convert',data={'type':url.split('/')[2],'_id':id[0],'v_id':url.split('/')[3],'ajax':'1','token':'','ftype':'mp3','fquality':'128'}).json()['result'],'html.parser').find('a')['href']
			return {
				'status': 200,
				'restapi' : 'ferdiz-afk',
				'scrap' :  'youtube',
				'title': title,
				'thumb': thumb,
				'filesize': filesize,
				'result': dl_link,
				'ext': 'mp3'
			}
		except Exception as e:
			print('Error : %s' % e)
			return {
				'status': False,
				'error': '[❗] Terjadi kesalahan mungkin link yang anda kirim tidak valid!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}



@app.route('/api/dewabatch', methods=['GET','POST'])
def dewabatch():
	if request.args.get('q'):
		try:
			q = request.args.get('q')
			he=search_dewabatch(quote(q))
			dewabatch=cari(he)
			if he != '':
				return {
					'status': 200,
					'sinopsis': dewabatch['result'],
					'thumb': dewabatch['cover'],
					'result': dewabatch['info']
				}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': 'Anime %s Tidak di temukan!' % unquote(q)
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/komiku', methods=['GET','POST'])
def komiku():
    if request.args.get('q'):
        try:
            q = request.args.get('q')
            komi = search_komiku(q)
            if 'Tidak di temukan' not in komi:
                manga = scrap_komiku(komi)
                return {
                    'status': 200,
                    'info': manga['info'],
                    'genre': manga['genre'],
                    'sinopsis': manga['sinopsis'],
                    'thumb': manga['thumb'],
                    'link_dl': manga['dl_link']
                }
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Manga %s Tidak di temukan' % unquote(q)
            }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter q'
        }

@app.route('/api/kuso', methods=['GET','POST'])
def kusonime():
	if request.args.get('q'):
		try:
			q = request.args.get('q')
			he=search_kusonime(quote(q))
			kuso=scrap_kusonime(he)
			if he != '':
				return {
					'status': 200,
					'sinopsis': kuso['sinopsis'],
					'thumb': kuso['thumb'],
					'info': kuso['info'],
					'title': kuso['title'],
					'link_dl': kuso['link_dl']
				}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': 'Anime %s Tidak di temukan' % unquote(q)
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/otakudesu')
def otakudesuu():
    if request.args.get('q'):
        try:
            q = request.args.get('q')
            he=search_otakudesu(quote(q))
            if he != '':
                otaku=scrap_otakudesu(he)
                return {
                    'status': 200,
                    'sinopsis': otaku['sinopsis'],
                    'thumb': otaku['thumb'],
                    'info': otaku['info'],
                    'title': otaku['title']
                }
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Anime %s Tidak di temukan' % unquote(q)
            }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter q'
        }
            
@app.route('/api/brainly', methods=['GET','POST'])
def brainly_scraper():
	if request.args.get('q'):
		try:
			query = request.args.get('q')
			br=brainly(gsearch('"%s" site:brainly.co.id' % quote(query), lang='id')[0])
			return {
				'status': 200,
				'result': br
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Pertanyaan %s tidak dapat saya temukan di brainly' % unquote(query)
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}
	


@app.route('/api/waifu', methods=['GET','POST'])
def waifu():
	scrap = bs(get('https://mywaifulist.moe/random').text, 'html.parser')
	a = json.loads(scrap.find('script', attrs={'type':'application/ld+json'}).string)
	desc = bs(get(a['url']).text, 'html.parser').find('meta', attrs={'property':'og:description'}).attrs['content']
	result = json.loads(bs(get(a['url']).text, 'html.parser').find('script', attrs={'type':'application/ld+json'}).string)
	if result['gender'] == 'female':
		return {
			'status': 200,
			'restapi' : 'ferdiz-afk',
			'name': result['name'],
			'desc': desc,
			'image': result['image'],
			'source': result['url']
		}
	else:
		return {
			'status': 200,
			'name': '%s (husbu)' % result['name'],
			'desc': desc,
			'image': result['image'],
			'source': result['url']
		}



@app.route('/api', methods=['GET','POST'])
def api():
	return render_template('api.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
	return render_template('profile.html')

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

HTTP_STATUS_CODES = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",  # see RFC 8297
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi Status",
    208: "Already Reported",  # see RFC 5842
    226: "IM Used",  # see RFC 3229
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    306: "Switch Proxy",  # unused
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",  # unused
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request Entity Too Large",
    414: "Request URI Too Long",
    415: "Unsupported Media Type",
    416: "Requested Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",  # see RFC 2324
    421: "Misdirected Request",  # see RFC 7540
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",  # see RFC 8470
    426: "Upgrade Required",
    428: "Precondition Required",  # see RFC 6585
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    449: "Retry With",  # proprietary MS extension
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",  # see RFC 2295
    507: "Insufficient Storage",
    508: "Loop Detected",  # see RFC 5842
    510: "Not Extended",
    511: "Network Authentication Failed",  # see RFC 6585
}

@app.errorhandler(404)
def error(e):
	return render_template('error.html'), 404
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT','5000')),debug=True)
