from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

card1to49 = [['士別','徳政令','おはらい','うんち','ぶっとび周遊','ぶっとび','特急周遊','特急'],
['浦河','刀狩り','乗っ取り','強奪飛び','スペシャル','物件飛び','新幹線周遊','急行周遊'],
['弟子屈','バキューム','徳政令','お殿様','ブックマーク','うんち','ぶっとび','急行'],
['知床','乗っ取り','徳政令','シュレッダー','テレポート','☆飛び','のぞみ'],
['岩見沢','福袋','期間延長','徳政令','おはらい','ぶっとび周遊','特急周遊'],
['宮古','徳政令','スペシャル','テレポート','物件飛び','ロイヤルEX','特急周遊'],
['恐山','徳政令','おはらい','足踏み','ぶっとび','特急周遊','急行周遊','特急'],
['新庄','徳政令','おはらい','足踏み','ぶっとび','特急周遊','急行周遊','特急'],
['三宅島','最果て','あっちいけ','牛歩','お役ごめん','君がすべて！','オール６','孤軍奮闘','特急'],
['大網','刀狩り','徳政令','☆飛び','北へ！','ぶっとび','特急周遊','新幹線'],
['日光','徳政令','おはらい','足踏み','ぶっとび','特急周遊','急行周遊','特急'],
['高輪ゲートウェイ','カードバンク','徳政令','物件飛び','ロイヤルEX','のぞみ周遊','リニア'],
['八尾','徳政令','イエロー','シュレッダー','北へ！','ぶっとび','特急周遊','特急'],
['佐久間','新幹線周遊','特急周遊','急行周遊','のぞみ','新幹線','特急','急行'],
['珠洲','オナラ','うんちの壁','もれちゃうぞ','うんち突入','指定うんち！','うんち','新幹線'],
['大月','徳政令','おはらい','足踏み','ぶっとび','特急周遊','急行周遊','特急'],
['木曽','徳政令','おはらい','足踏み','ぶっとび','特急周遊','急行周遊','特急'],
['マキノ','徳政令','イエロー','シュレッダー','北へ！','ぶっとび','特急周遊','特急'],
['綾部','刀狩り','徳政令','☆飛び','北へ！','ぶっとび','特急周遊','新幹線'],
['尾鷲','オナラ','うんちの壁','もれちゃうぞ','うんち突入','指定うんち！','うんち','新幹線'],
['益田','徳政令','おはらい','足踏み','ぶっとび','特急周遊','急行周遊','特急'],
['新居浜','スペシャル','おはらい','シュレッダー','☆飛び','物件飛び','特急周遊','新幹線'],
['中村','徳政令','おはらい','足踏み','ぶっとび','特急周遊','急行周遊','特急'],
['牛深','徳政令','イエロー','シュレッダー','北へ！','ぶっとび','特急周遊','特急'],
['高千穂','スペシャル','おはらい','シュレッダー','☆飛び','物件飛び','特急周遊','新幹線'],
['日向','バキューム','徳政令','お殿様','ブックマーク','うんち','ぶっとび','急行'],
['指宿','刀狩り','徳政令','☆飛び','北へ！','ぶっとび','特急周遊','新幹線'],
['佐多','絶好調崩し','ダビング','期間延長','徳政令','北へ！'],
['糸満','徳政令','イエロー','シュレッダー','北へ！','ぶっとび','特急周遊','特急'],
['赤嶺','刀狩り','乗っ取り','強奪飛び','スペシャル','物件飛び','新幹線周遊','急行周遊'],
['飫肥','徳政令','おはらい','足踏み','ぶっとび','特急周遊','急行周遊','特急']]
def search(a):
    b = []
    for i in range (31):
        for j in range (len(card1to49[i])):
            if a == card1to49[i][j]:
                if j == 0:
                    b.append(card1to49[i])
                else:
                    b.append(card1to49[i][0])
    return b

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
 
@bot.command()
async def neko(ctx):
    await ctx.send('nyan')
    
@bot.command()
async def cs(ctx,arg):
    await ctx.send(search(arg))

aa = [['--', 0, 0], ['土浦', 32000, 2100], ['小城', 5000, 2500], ['名寄', 13000, 2600], ['陸別', 106000, 2600], 
      ['美幌', 21000, 3000], ['淡路島', 50500, 3600], ['八丈島', 20000, 3800], ['大久保', 53000, 4000], ['遠野', 23000, 4200], 
      ['菜の花', 33000, 4200], ['舞鶴', 7000, 4300], ['伊豆大島', 43000, 4300], ['小淵沢', 52000, 4400], ['うるま', 21000, 4600], 
      ['笠間', 37000, 4600], ['天塩', 61000, 4600], ['千曲', 25000, 5000], ['天童', 70000, 5000], ['登別', 210000, 5000], 
      ['さぬき', 84000, 5200], ['岩国', 43000, 5400], ['斜里', 36000, 5500], ['八雲', 14000, 5600], ['浜田', 52000, 5600], 
      ['枕崎', 102000, 5600], ['大船渡', 23000, 5800], ['種子島', 31000, 5800], ['桜島', 34000, 5800], ['気仙沼', 43000, 5800], 
      ['森', 3000, 6000], ['金武', 3000, 6000], ['浜頓別', 211000, 6300], ['角館', 222000, 6400], ['宇都宮', 20000, 6500],
      ['山形', 79000, 6600], ['遠軽', 53000, 6700], ['喜多方', 5000, 7000], ['安芸', 56000, 7000], ['秋月', 72000, 7000], 
      ['足寄', 110000, 7000], ['糸魚川', 142000, 7000], ['八代', 65000, 7100], ['土岐', 240000, 7200], ['中津', 63000, 7400], 
      ['倉敷', 143000, 7400], ['岐 阜', 74000, 7500], ['御坊', 131000, 7500], ['下田', 14000, 7800], ['日生', 34000, 7800], 
      ['新宮', 68000, 7800], ['出雲', 8000, 8000], ['橿原', 23000, 8000], ['田子', 40000, 8000], ['明石', 64000, 8000], 
      ['松江', 79000, 8000], ['仙崎', 113000, 8000], ['伊豆高原', 175000, 8000], ['松島', 5000, 8200], ['沼田', 14000, 8200], 
      ['長万部', 82000, 8200], ['伊万里', 100000, 8200], ['会津若松', 124000, 8200], ['大分', 41000, 8600], ['盛岡', 16000, 8700],
      ['大宜味', 58000, 8800], ['米沢', 60000, 8800], ['竜飛', 262000, 9000], ['唐津', 33000, 9200], ['蒜山', 92000, 9200], 
      ['敦賀', 120000, 9200], ['むつ', 34000, 9400], ['名取', 47000, 9500], ['和歌山', 46000, 9800], ['氷見', 65000, 9800], 
      ['佐原', 106000, 9800], ['小田原', 5000, 10000], ['黒石', 24000, 10000], ['飯塚', 34000, 10000], ['奄美大島', 151000, 10000], 
      ['土佐清水', 170000, 10200], ['別府', 245000, 10300], ['対馬', 92000, 10400], ['石巻', 253000, 10400], ['三田', 101000, 10600],
      ['池田', 422000, 10600], ['宮 島', 17000, 10800], ['小浜', 8000, 11000], ['都城', 140000, 11000], ['興部', 182000, 11200], 
      ['北茨城', 134000, 11400], ['花巻', 242000, 11400], ['柳井', 282000, 11600], ['出石', 25500, 11800], ['和寒', 170000, 11800], 
      ['別海', 131000, 12200], ['金木', 155000, 12200], ['射水', 183000, 12200], ['村上', 362000, 12200], ['岸和田', 214000, 12300], 
      ['摩周', 83000, 12400], ['秋田', 21100, 12500], ['中札内', 110000, 12600], ['八戸', 212000, 12600], ['伊賀', 195000, 12800], 
      ['阿寒', 21000, 13000], ['鳥取', 65000, 13080], ['江差', 204000, 13200], ['鶴橋', 9000, 13600], ['厚岸', 122000, 13600], 
      ['銚子', 335000, 13600], ['横手', 204000, 13800], ['名護', 243000, 13800], ['利尻', 83000, 14000], ['松前', 163000, 14000],
      ['女川', 203000, 14000], ['安来', 153200, 14200], ['郡上', 234000, 14200], ['竹田', 110000, 14400], ['有田', 641000, 14400], 
      ['那須', 166000, 14500], ['久慈', 13000, 14700], ['鹿屋', 147000, 15500], ['礼文', 141000, 15600], ['中標津', 200000, 16000], 
      ['定山渓', 400000, 16000], ['彦根', 121000, 16200], ['ススキノ', 234000, 16200], ['赤穂', 242000, 16200], ['松本', 106000, 16800], 
      ['石垣島', 141000, 17600], ['宇和島', 148000, 17600], ['小樽', 152000, 17600], ['平泉', 213000, 17800], ['人吉', 443000, 17800],
      ['佐渡', 93000, 18000], ['常滑', 321000, 18000], ['和倉温泉', 803000, 18000], ['静岡', 154000, 18100], ['網走', 522000, 18600], 
      ['郡山', 407000, 18800], ['砂川', 113000, 19000], ['五條', 112000, 19200], ['北見', 119000, 19200], ['鹿児島', 187000, 19400], 
      ['東尋坊', 631000, 19600], ['帯広', 166000, 20000], ['須崎', 421000, 20200], ['四万十川', 97000, 20600], ['稚内', 551000, 20700],
      ['中津川', 423000, 21000], ['鴨川', 609000, 21000], ['佐賀', 374000, 21600], ['紋別', 260000, 22000], ['留萌', 350000, 22000], 
      ['糸島', 63000, 22200], ['高知', 285000, 22200], ['増毛', 320000, 22400], ['屋久島', 416000, 23200], ['鳴子', 1022000, 23500], 
      ['松阪', 400000, 24000], ['富士吉田', 804000, 24000], ['水俣', 834000, 24000], ['魚沼', 250000, 25200], ['壱岐', 211000, 25600], 
      ['生口島', 191000, 26000], ['久米島', 355000, 26500], ['松崎', 165000, 27400], ['鳥羽', 330000, 27600], ['近江八幡', 593000, 27600], 
      ['桐生', 705000, 27600], ['駒ヶ根', 112000, 28000], ['室蘭', 603000, 28200], ['甲府', 354000, 28400], ['呉', 895000, 28600], 
      ['小布施', 94000, 28800], ['高山', 385000, 28800], ['夕張', 555000, 28800], ['富良野', 911000, 28800], ['鶴岡', 348000, 29300],
      ['弘前', 71000, 30000], ['津和野', 360000, 30000], ['知覧', 376000, 30000], ['白浜', 863000, 30900], ['富士宮', 1108000, 34300],
      ['大根島', 145000, 34500], ['上川', 872000, 35400], ['五島', 182000, 35600], ['萩', 405000, 36000], ['襟裳', 300000, 37800], 
      ['湯布院', 812000, 38000], ['岡崎', 1200000, 38400], ['宮崎', 525000, 38600], ['鎌倉', 899000, 38800], ['宮古島', 901000, 39200], 
      ['高崎', 1406000, 39600], ['三沢', 1104000, 40000], ['湯田温泉', 552000, 40200], ['大三島', 890000, 41000], ['鯖江', 130000, 42400],
      ['天草', 362000, 43000], ['西都', 248000, 43400], ['福島', 2030000, 43900], ['修善寺', 1318000, 44200], ['下関', 872000, 46000], 
      ['上越', 1202000, 47200], ['祇園', 210000, 48000], ['根室', 383000, 48200], ['館山', 1820000, 48600], ['太宰府', 2304000, 50000], 
      ['五所川原', 350000, 50400], ['深谷', 148000, 50560], ['白馬', 2600000, 52000], ['水戸', 2355000, 52500], ['津', 705000, 52800],
      ['長浜',1820000, 52800], ['芽室', 360000, 54000], ['栃木', 672000, 54600], ['長岡', 1851000, 54800], ['大間', 254000, 55800], 
      ['奈良',855000,56300], ['三戸', 125000, 56400], ['門司港', 1803000, 58500], ['城崎', 561000, 60000], ['青森', 1656000, 62200],
      ['三島', 827000,63500], ['富山', 681000, 64000], ['苫小牧', 2106000, 64000], ['高松', 1474000, 64400], ['茂木', 61000, 65800], 
      ['いわき',2202000,66000], ['長野', 2657000, 66700], ['軽井沢', 1320000, 69400], ['諫早', 481000, 69800], ['美瑛', 960000, 75000],
      ['羅臼',400000,76000], ['湯河原', 581000, 76200], ['石見銀山', 1003000, 79600], ['草津', 1551000, 83200],
      ['湯沢',4100000,84000], ['八王子', 2491000, 87400], ['本部', 2023000, 87600], ['酒田', 1217000, 89300], ['長崎', 445000, 89400], 
      ['道後',3024000,89500], ['箱根', 2413000, 90000], ['新潟', 4093000, 90800], ['熱海', 2915000, 91000], ['那覇', 1635000, 91800], 
      ['余市',1050000, 93600], ['松山', 2457000, 94500], ['中華街', 960000, 96000], ['有馬', 702000, 98000], 
      ['秋葉原',2481000,101800], ['堺', 623000, 103800], ['福井', 970000, 103800], ['伊勢', 2143000, 104000], ['嵐山', 720000, 105200],
      ['佐世保',4413000,109800], ['ひたちなか', 1632000, 111200], ['高 岡', 2783000, 113600], ['安城', 4002000, 114000],
      ['小倉', 1606000,118200], ['境港', 1001000, 119000], ['香林坊', 2836000, 120000], ['旭川', 1323000, 122600], 
      ['釧路', 2702000,123000], ['茶屋街', 1557000, 124200], ['今治', 4814000, 134100], ['徳島', 1653000, 135800], 
      ['函館', 899000, 137200], ['豊橋', 3300000, 151280], ['鳥栖', 2110000, 151600], ['金沢', 2420000, 152800],
      ['さいたま',7002000,162000], ['広島', 4835000, 168800], ['栄', 2037000, 171000], ['四国中央', 6020000, 177600], 
      ['上田', 1262000, 185120], ['上野', 5450000, 186000], ['秩父', 3053000, 187000], ['大阪', 1714000, 188600], 
      ['坂出', 6742000, 190000], ['ホノルル', 4162000, 201000], ['船橋', 5054000, 212800], ['中洲', 10164000, 221400], 
      ['仙台', 5556000, 221600], ['後楽園', 6400000, 224000], ['京橋', 1151000, 225600], ['博多', 2443000, 250200], 
      ['小松', 6473000, 272200], ['前橋', 6553000, 274200], ['福知山', 2142000, 283100], ['日本橋', 8920000, 283400], 
      ['札幌', 5983000, 286400], ['原宿', 10680000, 308800], ['山口', 3294000, 317800], ['ニセコ', 3201000, 321000], 
      ['大津', 4394000, 325600], ['瀬戸', 3442000, 345600], ['鞆の浦', 17101000, 348200], ['渋谷', 4206000, 352000], 
      ['吹田', 5181000, 353200], ['福山', 8241000, 366500], ['千葉', 18150000, 375400], ['洞爺湖', 7382000, 430800],
      ['銀座', 17770000, 497400], ['浜松', 7083000, 515000], ['四日市', 9981000, 519800], ['熊谷', 8853000, 536200], 
      ['久留米', 13123000, 550400], ['神戸', 9412000, 552400], ['天王寺', 14205000, 566600], ['名古屋港', 9440000, 598200],
      ['なんば', 7313000, 647200], ['東京', 21401000, 670000], ['お台場', 28900000, 670000], ['釜石', 40232000, 813200], 
      ['名古屋', 19114000, 844000], ['宇部', 12711000, 985600], ['鳴門', 8661000, 1055800], ['熊本', 27902000, 1297880], 
      ['横須賀', 31008000, 1480600], ['姫路', 34053000, 1889800], ['天保山', 42420000, 2005200], ['日田', 33653000, 2011400], 
      ['尾道', 30392000, 2432000], ['新宿', 28720000, 2513200], ['北浜', 33110000, 2676800], [' 川崎', 50801000, 2819000], 
      ['登米', 70810000, 2826000], ['千駄ヶ谷', 22734000, 3316200], ['横浜', 84532000, 4246000], ['豊田', 74582000, 4295000], 
      ['品川', 105401000, 5041700], ['京都', 79710000, 6800000], ['門真', 41990000, 8153200], ['幕張', 217700000, 17292000],
      ['浅草', 63831000, 25443200], ['岡山', 1000013000, 120034600]]

def bukkeneki(b):
    for i in range(len(aa)):
        if b == aa[i][0]:
            ans = aa[i][0] + '独占購入額' + str(aa[i][1]) + '万円 独占時収益' + str(aa[i][2]) + '万円'
    return ans

@bot.command()
async def bs(ctx,arg):
    await ctx.send(bukkeneki(arg))

def dokusen(ctx,c):
    count = 0
    i = 0
    while count < 15 and i < 339:
        if c > aa[339-i][1]:
            ans = aa[339-i][0] + '独占購入額' + str(aa[339-i][1]) + '万円 独占時収益' + str(aa[339-i][2]) + '万円'
            count += 1
            ctx.send(ans)
        i += 1
    return

@bot.command()
async def ds(ctx,arg):
    await dokusen(ctx,int(arg))
                   
bot.run(token)
