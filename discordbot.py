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
['高輪ゲートウェイ','カードバンクカード','徳政令','物件飛び','ロイヤルEX','のぞみ周遊','リニア'],
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
    for i in range (30):
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
async def cs(ctx,arg):
    await ctx.send(search(arg))

bot.run(token)
