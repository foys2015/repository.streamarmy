import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,hashlib,timeimport base64import HTMLParserimport osfrom resources.libs.modules import satoolsfrom resources.libs.modules.scrapers import cinemafrom resources.libs.modules.scrapers import threetwoonefrom resources.libs.modules.scrapers import newmoviesfrom resources.libs.modules.scrapers import fmoviesaddon_id        = 'plugin.video.streamarmy'AddonTitle      = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))dialog          = xbmcgui.Dialog()dp              = xbmcgui.DialogProgress()def MULTI_SEARCH_SCRAPERS(url='None'):        if url == 'None':        string =''        keyboard = xbmc.Keyboard(string, 'Enter Search Term')        keyboard.doModal()        if keyboard.isConfirmed():            string = keyboard.getText()            if len(string)>1:                term = string.lower()                            else: quit()    else: term = urllib.unquote_plus(url).lower(); string = urllib.unquote_plus(url)    current = 0    totalsites = 4    dp.create(AddonTitle, '[COLOR yellow]Searching for ' + string.title())    dp.update(0)    current = current + 1    progress = 100 * int(current)/int(totalsites)    dp.update(progress, '','[COLOR yellowgreen]Searching 123 Movies','[COLOR silver]Source ' + str(current) + ' of ' + str(totalsites) + '[/COLOR]')    time.sleep(2)    try:        term_123Movies = term.replace(' ', '+')         url="http://123movies.net/search-movies/" + term_123Movies + '.html'        cinema.SCRAPE_123MOVIES_SEARCH(url + "|SPLIT|" + string)    except: pass    current = current + 1    progress = 100 * int(current)/int(totalsites)    dp.update(progress, '','[COLOR yellowgreen]Currently searching 321Movies.com...','[COLOR silver]Source ' + str(current) + ' of ' + str(totalsites) + '[/COLOR]')    try:        term_321Movies = term.replace(' ', '+')           url="https://321movies.cc/?s=" + term_321Movies        threetwoone.SCRAPE_321MOVIES_CONTENT(url + "|SPLIT|" + string)    except: pass    current = current + 1    progress = 100 * int(current)/int(totalsites)    dp.update(progress, '','[COLOR yellowgreen]Currently searching New Movies Online...','[COLOR silver]Source ' + str(current) + ' of ' + str(totalsites) + '[/COLOR]')    try:        term_newmoviesonline = term.replace(' ', '+')        url="http://newmoviesonline.ws/?s=" + term_newmoviesonline        newmovies.SCRAPE_NEWMOVIESONLINE_CONTENT(url)    except: pass    current = current + 1    progress = 100 * int(current)/int(totalsites)    dp.update(progress, '','[COLOR yellowgreen]Searching FMovies','[COLOR silver]Source ' + str(current) + ' of ' + str(totalsites) + '[/COLOR]')    time.sleep(2)    try:        term_FMovies = term.replace(' ', '+')         url="http://fmovie.io/search.html?keyword=" + term_FMovies        fmovies.SCRAPE_FMOVIES_CONTENT(url)    except: pass    