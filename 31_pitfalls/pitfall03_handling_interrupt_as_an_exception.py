###
#	no interrupt handling / wrong interrupt handling
###

'''
	most dumbest way to handle a signal:
'''
try:
	print('Waiting patiently...')

	while True:
		pass
	#end while
except KeyboardInterrupt as ke:
	print(f'interrupted process, because... {ke.args}')
#end try

'''
	A signal and an exception have some similar behavior. It pauses / stops
	your application. However, a signal can't be handled as an exception.
	In that case only Ctrl+C can be "handled" without any information.
	Any other signal is unable to handle by that code above.

	Because an exception triggers always at the same time,
	an interrupt can appear at any time.

	this is the way to go:
'''
import signal as sig

#	usually, a global object shall not be used => could contain side effect(s)
onContinue: bool = True

#	handling the incoming signal, which has also be registered before
def handler(signal, frame) -> None:
	msg = f'''
	I got that signal:	{sig.Signals(signal).name}
	the signal number:	{signal}
	signal location: 	{frame}
	'''
	print(msg)

	global onContinue
	onContinue = False
#end function

def main() -> None:
	#	register some possibly incoming signals during runtime
	#	SIGINT	=>	CTRL + C
	#	SIGTERM	=>	terminate the application in command line (without kill -9)
	sig.signal(sig.SIGINT, handler)
	sig.signal(sig.SIGTERM, handler)

	print('Waiting patiently...')
	while onContinue:
		pass
	#end function

	print('Finally!')
#end function

if __name__ == '__main__':
	main()
#end entry point
