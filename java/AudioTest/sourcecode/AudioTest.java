import at.*;

class AudioTest {

	static String os;
	static String ln;

	public static void main(String[] args) throws Exception{
		AudioControl audioControl;
		audioControl = new AudioControl();
		try {
			//Se puede correr una prueba de AudioControl por terminal pasando el argumento "terminal"
			if (args[0].equals("terminal")){
				int m[] = {0,0,0,0};
				int l[] = {0,0,0,0};
				audioControl.setConfig(4, m, l);
				audioControl.play();
			}
		} catch (Exception e) {
			//Creamos las ventana de control...
			Interface i = new Interface(audioControl);
		}
	}

}
