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

a =[]
for i in range(340):
    a.append(0)
a[0] = '-- 0 0'
a[1]	=	'土浦	32000	2100'
a[2]	=	'小城	5000	2500'
a[3]	=	'名寄	13000	2600'
a[4]	=	'陸別	106000	2600'
a[5]	=	'美幌	21000	3000'
a[6]	=	'淡路島	50500	3600'
a[7]	=	'八丈島	20000	3800'
a[8]	=	'大久保	53000	4000'
a[9]	=	'遠野	23000	4200'
a[10]	=	'菜の花	33000	4200'
a[11]	=	'舞鶴	7000	4300'
a[12]	=	'伊豆大島	43000	4300'
a[13]	=	'小淵沢	52000	4400'
a[14]	=	'うるま	21000	4600'
a[15]	=	'笠間	37000	4600'
a[16]	=	'天塩	61000	4600'
a[17]	=	'千曲	25000	5000'
a[18]	=	'天童	70000	5000'
a[19]	=	'登別	210000	5000'
a[20]	=	'さぬき	84000	5200'
a[21]	=	'岩国	43000	5400'
a[22]	=	'斜里	36000	5500'
a[23]	=	'八雲	14000	5600'
a[24]	=	'浜田	52000	5600'
a[25]	=	'枕崎	102000	5600'
a[26]	=	'大船渡	23000	5800'
a[27]	=	'種子島	31000	5800'
a[28]	=	'桜島	34000	5800'
a[29]	=	'気仙沼	43000	5800'
a[30]	=	'森	3000	6000'
a[31]	=	'金武	3000	6000'
a[32]	=	'浜頓別	211000	6300'
a[33]	=	'角館	222000	6400'
a[34]	=	'宇都宮	20000	6500'
a[35]	=	'山形	79000	6600'
a[36]	=	'遠軽	53000	6700'
a[37]	=	'喜多方	5000	7000'
a[38]	=	'安芸	56000	7000'
a[39]	=	'秋月	72000	7000'
a[40]	=	'足寄	110000	7000'
a[41]	=	'糸魚川	142000	7000'
a[42]	=	'八代	65000	7100'
a[43]	=	'土岐	240000	7200'
a[44]	=	'中津	63000	7400'
a[45]	=	'倉敷	143000	7400'
a[46]	=	'岐阜	74000	7500'
a[47]	=	'御坊	131000	7500'
a[48]	=	'下田	14000	7800'
a[49]	=	'日生	34000	7800'
a[50]	=	'新宮	68000	7800'
a[51]	=	'出雲	8000	8000'
a[52]	=	'橿原	23000	8000'
a[53]	=	'田子	40000	8000'
a[54]	=	'明石	64000	8000'
a[55]	=	'松江	79000	8000'
a[56]	=	'仙崎	113000	8000'
a[57]	=	'伊豆高原	175000	8000'
a[58]	=	'松島	5000	8200'
a[59]	=	'沼田	14000	8200'
a[60]	=	'長万部	82000	8200'
a[61]	=	'伊万里	100000	8200'
a[62]	=	'会津若松	124000	8200'
a[63]	=	'大分	41000	8600'
a[64]	=	'盛岡	16000	8700'
a[65]	=	'大宜味	58000	8800'
a[66]	=	'米沢	60000	8800'
a[67]	=	'竜飛	262000	9000'
a[68]	=	'唐津	33000	9200'
a[69]	=	'蒜山	92000	9200'
a[70]	=	'敦賀	120000	9200'
a[71]	=	'むつ	34000	9400'
a[72]	=	'名取	47000	9500'
a[73]	=	'和歌山	46000	9800'
a[74]	=	'氷見	65000	9800'
a[75]	=	'佐原	106000	9800'
a[76]	=	'小田原	5000	10000'
a[77]	=	'黒石	24000	10000'
a[78]	=	'飯塚	34000	10000'
a[79]	=	'奄美大島	151000	10000'
a[80]	=	'土佐清水	170000	10200'
a[81]	=	'別府	245000	10300'
a[82]	=	'対馬	92000	10400'
a[83]	=	'石巻	253000	10400'
a[84]	=	'三田	101000	10600'
a[85]	=	'池田	422000	10600'
a[86]	=	'宮島	17000	10800'
a[87]	=	'小浜	8000	11000'
a[88]	=	'都城	140000	11000'
a[89]	=	'興部	182000	11200'
a[90]	=	'北茨城	134000	11400'
a[91]	=	'花巻	242000	11400'
a[92]	=	'柳井	282000	11600'
a[93]	=	'出石	25500	11800'
a[94]	=	'和寒	170000	11800'
a[95]	=	'別海	131000	12200'
a[96]	=	'金木	155000	12200'
a[97]	=	'射水	183000	12200'
a[98]	=	'村上	362000	12200'
a[99]	=	'岸和田	214000	12300'
a[100]	=	'摩周	83000	12400'
a[101]	=	'秋田	21100	12500'
a[102]	=	'中札内	110000	12600'
a[103]	=	'八戸	212000	12600'
a[104]	=	'伊賀	195000	12800'
a[105]	=	'阿寒	21000	13000'
a[106]	=	'鳥取	65000	13080'
a[107]	=	'江差	204000	13200'
a[108]	=	'鶴橋	9000	13600'
a[109]	=	'厚岸	122000	13600'
a[110]	=	'銚子	335000	13600'
a[111]	=	'横手	204000	13800'
a[112]	=	'名護	243000	13800'
a[113]	=	'利尻	83000	14000'
a[114]	=	'松前	163000	14000'
a[115]	=	'女川	203000	14000'
a[116]	=	'安来	153200	14200'
a[117]	=	'郡上	234000	14200'
a[118]	=	'竹田	110000	14400'
a[119]	=	'有田	641000	14400'
a[120]	=	'那須	166000	14500'
a[121]	=	'久慈	13000	14700'
a[122]	=	'鹿屋	147000	15500'
a[123]	=	'礼文	141000	15600'
a[124]	=	'中標津	200000	16000'
a[125]	=	'定山渓	400000	16000'
a[126]	=	'彦根	121000	16200'
a[127]	=	'ススキノ	234000	16200'
a[128]	=	'赤穂	242000	16200'
a[129]	=	'松本	106000	16800'
a[130]	=	'石垣島	141000	17600'
a[131]	=	'宇和島	148000	17600'
a[132]	=	'小樽	152000	17600'
a[133]	=	'平泉	213000	17800'
a[134]	=	'人吉	443000	17800'
a[135]	=	'佐渡	93000	18000'
a[136]	=	'常滑	321000	18000'
a[137]	=	'和倉温泉	803000	18000'
a[138]	=	'静岡	154000	18100'
a[139]	=	'網走	522000	18600'
a[140]	=	'郡山	407000	18800'
a[141]	=	'砂川	113000	19000'
a[142]	=	'五條	112000	19200'
a[143]	=	'北見	119000	19200'
a[144]	=	'鹿児島	187000	19400'
a[145]	=	'東尋坊	631000	19600'
a[146]	=	'帯広	166000	20000'
a[147]	=	'須崎	421000	20200'
a[148]	=	'四万十川	97000	20600'
a[149]	=	'稚内	551000	20700'
a[150]	=	'中津川	423000	21000'
a[151]	=	'鴨川	609000	21000'
a[152]	=	'佐賀	374000	21600'
a[153]	=	'紋別	260000	22000'
a[154]	=	'留萌	350000	22000'
a[155]	=	'糸島	63000	22200'
a[156]	=	'高知	285000	22200'
a[157]	=	'増毛	320000	22400'
a[158]	=	'屋久島	416000	23200'
a[159]	=	'鳴子	1022000	23500'
a[160]	=	'松阪	400000	24000'
a[161]	=	'富士吉田	804000	24000'
a[162]	=	'水俣	834000	24000'
a[163]	=	'魚沼	250000	25200'
a[164]	=	'壱岐	211000	25600'
a[165]	=	'生口島	191000	26000'
a[166]	=	'久米島	355000	26500'
a[167]	=	'松崎	165000	27400'
a[168]	=	'鳥羽	330000	27600'
a[169]	=	'近江八幡	593000	27600'
a[170]	=	'桐生	705000	27600'
a[171]	=	'駒ヶ根	112000	28000'
a[172]	=	'室蘭	603000	28200'
a[173]	=	'甲府	354000	28400'
a[174]	=	'呉	895000	28600'
a[175]	=	'小布施	94000	28800'
a[176]	=	'高山	385000	28800'
a[177]	=	'夕張	555000	28800'
a[178]	=	'富良野	911000	28800'
a[179]	=	'鶴岡	348000	29300'
a[180]	=	'弘前	71000	30000'
a[181]	=	'津和野	360000	30000'
a[182]	=	'知覧	376000	30000'
a[183]	=	'白浜	863000	30900'
a[184]	=	'富士宮	1108000	34300'
a[185]	=	'大根島	145000	34500'
a[186]	=	'上川	872000	35400'
a[187]	=	'五島	182000	35600'
a[188]	=	'萩	405000	36000'
a[189]	=	'襟裳	300000	37800'
a[190]	=	'湯布院	812000	38000'
a[191]	=	'岡崎	1200000	38400'
a[192]	=	'宮崎	525000	38600'
a[193]	=	'鎌倉	899000	38800'
a[194]	=	'宮古島	901000	39200'
a[195]	=	'高崎	1406000	39600'
a[196]	=	'三沢	1104000	40000'
a[197]	=	'湯田温泉	552000	40200'
a[198]	=	'大三島	890000	41000'
a[199]	=	'鯖江	130000	42400'
a[200]	=	'天草	362000	43000'
a[201]	=	'西都	248000	43400'
a[202]	=	'福島	2030000	43900'
a[203]	=	'修善寺	1318000	44200'
a[204]	=	'下関	872000	46000'
a[205]	=	'上越	1202000	47200'
a[206]	=	'祇園	210000	48000'
a[207]	=	'根室	383000	48200'
a[208]	=	'館山	1820000	48600'
a[209]	=	'太宰府	2304000	50000'
a[210]	=	'五所川原	350000	50400'
a[211]	=	'深谷	148000	50560'
a[212]	=	'白馬	2600000	52000'
a[213]	=	'水戸	2355000	52500'
a[214]	=	'津	705000	52800'
a[215]	=	'長浜	1820000	52800'
a[216]	=	'芽室	360000	54000'
a[217]	=	'栃木	672000	54600'
a[218]	=	'長岡	1851000	54800'
a[219]	=	'大間	254000	55800'
a[220]	=	'奈良	855000	56300'
a[221]	=	'三戸	125000	56400'
a[222]	=	'門司港	1803000	58500'
a[223]	=	'城崎	561000	60000'
a[224]	=	'青森	1656000	62200'
a[225]	=	'三島	2827000	63500'
a[226]	=	'富山	681000	64000'
a[227]	=	'苫小牧	2106000	64000'
a[228]	=	'高松	1474000	64400'
a[229]	=	'茂木	61000	65800'
a[230]	=	'いわき	2202000	66000'
a[231]	=	'長野	2657000	66700'
a[232]	=	'軽井沢	1320000	69400'
a[233]	=	'諫早	481000	69800'
a[234]	=	'美瑛	960000	75000'
a[235]	=	'羅臼	400000	76000'
a[236]	=	'湯河原	581000	76200'
a[237]	=	'石見銀山	1003000	79600'
a[238]	=	'草津	1551000	83200'
a[239]	=	'湯沢	4100000	84000'
a[240]	=	'八王子	2491000	87400'
a[241]	=	'本部	2023000	87600'
a[242]	=	'酒田	1217000	89300'
a[243]	=	'長崎	445000	89400'
a[244]	=	'道後	3024000	89500'
a[245]	=	'箱根	2413000	90000'
a[246]	=	'新潟	4093000	90800'
a[247]	=	'熱海	2915000	91000'
a[248]	=	'那覇	1635000	91800'
a[249]	=	'余市	1050000	93600'
a[250]	=	'松山	2457000	94500'
a[251]	=	'中華街	960000	96000'
a[252]	=	'有馬	702000	98000'
a[253]	=	'秋葉原	2481000	101800'
a[254]	=	'堺	623000	103800'
a[255]	=	'福井	970000	103800'
a[256]	=	'伊勢	2143000	104000'
a[257]	=	'嵐山	720000	105200'
a[258]	=	'佐世保	4413000	109800'
a[259]	=	'ひたちなか	1632000	111200'
a[260]	=	'高岡	2783000	113600'
a[261]	=	'安城	4002000	114000'
a[262]	=	'小倉	1606000	118200'
a[263]	=	'境港	1001000	119000'
a[264]	=	'香林坊	2836000	120000'
a[265]	=	'旭川	1323000	122600'
a[266]	=	'釧路	2702000	123000'
a[267]	=	'茶屋街	1557000	124200'
a[268]	=	'今治	4814000	134100'
a[269]	=	'徳島	1653000	135800'
a[270]	=	'函館	899000	137200'
a[271]	=	'豊橋	3300000	151280'
a[272]	=	'鳥栖	2110000	151600'
a[273]	=	'金沢	2420000	152800'
a[274]	=	'さいたま	7002000	162000'
a[275]	=	'広島	4835000	168800'
a[276]	=	'栄	2037000	171000'
a[277]	=	'四国中央	6020000	177600'
a[278]	=	'上田	1262000	185120'
a[279]	=	'上野	5450000	186000'
a[280]	=	'秩父	3053000	187000'
a[281]	=	'大阪	1714000	188600'
a[282]	=	'坂出	6742000	190000'
a[283]	=	'ホノルル	4162000	201000'
a[284]	=	'船橋	5054000	212800'
a[285]	=	'中洲	10164000	221400'
a[286]	=	'仙台	5556000	221600'
a[287]	=	'後楽園	6400000	224000'
a[288]	=	'京橋	1151000	225600'
a[289]	=	'博多	2443000	250200'
a[290]	=	'小松	6473000	272200'
a[291]	=	'前橋	6553000	274200'
a[292]	=	'福知山	2142000	283100'
a[293]	=	'日本橋	8920000	283400'
a[294]	=	'札幌	5983000	286400'
a[295]	=	'原宿	10680000	308800'
a[296]	=	'山口	3294000	317800'
a[297]	=	'ニセコ	3201000	321000'
a[298]	=	'大津	4394000	325600'
a[299]	=	'瀬戸	3442000	345600'
a[300]	=	'鞆の浦	17101000	348200'
a[301]	=	'渋谷	4206000	352000'
a[302]	=	'吹田	5181000	353200'
a[303]	=	'福山	8241000	366500'
a[304]	=	'千葉	18150000	375400'
a[305]	=	'洞爺湖	7382000	430800'
a[306]	=	'銀座	17770000	497400'
a[307]	=	'浜松	7083000	515000'
a[308]	=	'四日市	9981000	519800'
a[309]	=	'熊谷	8853000	536200'
a[310]	=	'久留米	13123000	550400'
a[311]	=	'神戸	9412000	552400'
a[312]	=	'天王寺	14205000	566600'
a[313]	=	'名古屋港	9440000	598200'
a[314]	=	'なんば	7313000	647200'
a[315]	=	'東京	21401000	670000'
a[316]	=	'お台場	28900000	670000'
a[317]	=	'釜石	40232000	813200'
a[318]	=	'名古屋	19114000	844000'
a[319]	=	'宇部	12711000	985600'
a[320]	=	'鳴門	8661000	1055800'
a[321]	=	'熊本	27902000	1297880'
a[322]	=	'横須賀	31008000	1480600'
a[323]	=	'姫路	34053000	1889800'
a[324]	=	'天保山	42420000	2005200'
a[325]	=	'日田	33653000	2011400'
a[326]	=	'尾道	30392000	2432000'
a[327]	=	'新宿	28720000	2513200'
a[328]	=	'北浜	33110000	2676800'
a[329]	=	'川崎	50801000	2819000'
a[330]	=	'登米	70810000	2826000'
a[331]	=	'千駄ヶ谷	22734000	3316200'
a[332]	=	'横浜	84532000	4246000'
a[333]	=	'豊田	74582000	4295000'
a[334]	=	'品川	105401000	5041700'
a[335]	=	'京都	79710000	6800000'
a[336]	=	'門真	41990000	8153200'
a[337]	=	'幕張	217700000	17292000'
a[338]	=	'浅草	63831000	25443200'
a[339]	=	'岡山	1000013000	120034600'
				
for i in range(len(a)):
    a[i]=a[i].split()	
    a[i][1]=int(a[i][1])
    a[i][2]=int(a[i][2])

def bukkeneki(ctx,b):
    for i in range(len(a)):
        if b == a[i][0]:
            ans = "a[i][0],'独占購入額',a[i][1],'万円　独占時収益',a[i][2],'万円'"
	    ctx.send(ans)

def dokusen(ctx,c):
    count = 0
    i = 0
    while count < 15 or i > 339:
        if c > a[339-i][1]:
            ans ="a[339-i][0],'独占購入額',a[339-i][1],'万円　独占時収益',a[339-i][2],'万円'"
	    ctx.send(ans)
            count += 1
        i += 1

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

@bot.command()
async def bs(ctx,arg):
    await bukkeneki(ctx,arg)

@bot.command()
async def ds(ctx,arg):
    await dokusen(ctx,int(arg))
                   
bot.run(token)
