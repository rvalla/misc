import at.*;

class AudioTest {

	static String os;
	static String ln;

	public static void main(String[] args) throws Exception{
		AudioControl audioControl;
		audioControl = new AudioControl();
		try {
			if (args[0].equals("terminal")){
				int m[] = {0,0,0,0};
				int l[] = {0,0,0,0};
				audioControl.setConfig(4, m, l);
				audioControl.play();
			}
		} catch (Exception e) {
			//Esta es la clase que tiene la interfaz, por ahora recibe la clase audioControl por constructor
			Interface i = new Interface(audioControl);
		}
	}

}
