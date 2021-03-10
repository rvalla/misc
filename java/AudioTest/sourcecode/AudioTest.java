import at.*;

class AudioTest {

	static String os;
	static String ln;

	public static void main(String[] args) throws Exception{
		AudioControl audioControl = new AudioControl();
		Interface i = new Interface(audioControl);
	}

}
