package at;

import java.net.URL;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Mixer;
import javax.sound.sampled.Line;
import javax.sound.sampled.SourceDataLine;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.TargetDataLine;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;

public class AudioControl {

  private static final int BUFFER_SIZE = 2048 * 8;
	//private final byte[] buffers[] = new byte[BUFFER_SIZE][4];
	private final byte[] buffer = new byte[BUFFER_SIZE];

	private static Mixer.Info[] mixerInfo = AudioSystem.getMixerInfo();
	private ArrayList<Integer> mixerLocations = new ArrayList<Integer>(20);
	private ArrayList<String> mixersNames = new ArrayList<String>(20);

	private int nTest = 2;
	private AudioFormat af;
	private File files[] = new File[nTest];
	private AudioInputStream streams[] = new AudioInputStream[nTest];
	private SourceDataLine lines[] = new SourceDataLine[nTest];

	public AudioControl() {
		System.out.println("-- AudioControl: Some tests to play multichannel audio...");
		for (int i = 0; i < nTest; i++) {
			try {
				String filename = "audio/ch_" + String.valueOf(i+1) + ".wav";
				URL aux = getClass().getResource(filename);
				files[i] = new File(aux.toURI());
				streams[i] = AudioSystem.getAudioInputStream(files[i]);
				af = streams[i].getFormat();
				System.out.println("-- Seems ok...");
			} catch (Exception e) {
				throw new RuntimeException(e);
			}
		}
		for (int i = 0; i < mixerInfo.length; i++) {
			Mixer mixer = AudioSystem.getMixer(mixerInfo[i]);
			for (Line.Info l : mixer.getSourceLineInfo()) {
				if (l.toString().startsWith("interface SourceDataLine")){
					System.out.println("-- Adding a mixer...");
					mixerLocations.add(i);
					mixersNames.add(mixerInfo[i].getName());
				}
			}
		}
	}

	public String[] getMixers() {
		String result[] = new String[mixerLocations.size()];
		for (int i = 0; i < result.length; i++) {
			result[i] = mixersNames.get(i);
		}
		return result;
	}

	public String[] getLines() {
		String result[] = new String[8];
		for (int i = 0; i < result.length; i++) {
			result[i] = String.valueOf(i + 1);
		}
		return result;
	}

	public void triggerPlay(int tMixer[], int tChannels[]){
		System.out.println("-- Listos para reproducir...");
		Mixer mixers[] = new Mixer[nTest];
		for (int i = 0; i < nTest; i++) {
			try {
				mixers[i] = AudioSystem.getMixer(mixerInfo[mixerLocations.get(tMixer[i])]);
				Line.Info[] lInfo = mixers[i].getSourceLineInfo();
				lines[i] = (SourceDataLine) mixers[i].getLine(lInfo[tMixer[i]]);
				lines[i].open(af, BUFFER_SIZE);
				lines[i].start();
			} catch (LineUnavailableException ele) {
				System.out.println("Ups, the line...");
				throw new RuntimeException(ele);
			} catch (Exception e) {
				System.out.println("Ups, unknown...");
				throw new RuntimeException(e);
			}
		}
		play();
	}

	private void play(){
		try {
			while (streams[0].read(buffer) != -1) {
				for (int m = 0; m < nTest; m++) {
					lines[m].write(buffer, 0, buffer.length);
				}
			}
		} catch (Exception e) {
			System.out.println("Ups, the play...");
			throw new RuntimeException(e);
		}
	}

}
