import java.io.*;
import javax.sound.sampled.*;

class ListAudioDevices {

	static Mixer.Info[] mixerInfo = AudioSystem.getMixerInfo();
	static Mixer mixer;

	public static void main(String[] args) {
		for (int i = 0; i < mixerInfo.length; i++) {
			 	mixer = AudioSystem.getMixer(mixerInfo[i]);
				for(Line.Info lineInfo : mixer.getTargetLineInfo()){
					try {
						Line thisLine = mixer.getLine(lineInfo);
						thisLine.open();
						System.out.print("-- : ");
						System.out.print(thisLine);
						System.out.println("");
					} catch (Exception e) {
						System.out.println("No anda");
					}
				}
	    }
		}
}
