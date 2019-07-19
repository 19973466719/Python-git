import time
import win32com.client

dehua=win32com.client.Dispatch('SAPI.SPVOICE')



while 1:
    dehua.Speak('我同意你的观点')
    time.sleep(5)