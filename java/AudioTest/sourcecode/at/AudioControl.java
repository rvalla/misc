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
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.ArrayList;

public class AudioControl {

	private static final int BUFFER_SIZE = 2048 * 8;
	private final byte[] buffer = new byte[BUFFER_SIZE];

	private static Mixer.Info[] mixerInfo = AudioSystem.getMixerInfo();
	private ArrayList<Integer> mixerLocations = new ArrayList<Integer>(20); //Las direcciones de los mixers...
	private ArrayList<String> mixersNames = new ArrayList<String>(20); //Nombres de los mixers... para la interfaz...

	private AtomicBoolean playing = new AtomicBoolean();
	private int nTest = 4; // Este número define cuántos archivos, líneas carga (1-4)
	private AudioFormat af = new AudioFormat(44100.0f, 16, 1, true, false);
	private File files[] = new File[nTest]; //Los archivos de audio...
	private AudioInputStream streams[] = new AudioInputStream[nTest]; // Acá voy a cargar los archivos...
	private SourceDataLine lines[] = new SourceDataLine[nTest]; //Las líneas para reproducir...

	public AudioControl() {
		System.out.println("-- AudioControl: Some tests to play multichannel audio...");
		//Primero cargamos los archivos de audio...
		for (int i = 0; i < nTest; i++) {
			try {
				String filename = "audio/ch_" + String.valueOf(i + 1) + ".wav";
				URL aux = getClass().getResource(filename);
				files[i] = new File(aux.toURI());
				streams[i] = AudioSystem.getAudioInputStream(files[i]);
				System.out.println("-- Seems ok...");
			} catch (Exception e) {
				throw new RuntimeException(e);
			}
		}
		//Recorremos los mixers en el sistema y nos guardamos las líneas interface SourceDataLine...
		for (int i = 0; i < mixerInfo.length; i++) {
			Mixer mixer = AudioSystem.getMixer(mixerInfo[i]);
			for (Line.Info l : mixer.getSourceLineInfo()) {
				if (l.toString().startsWith("interface SourceDataLine")) {
					System.out.println("-- Adding a mixer...");
					mixerLocations.add(i);
					mixersNames.add(mixerInfo[i].getName());
				}
			}
		}
	}

	//Devolvemos un arreglo con los nombres de los mixers para la interfaz...
	public String[] getMixers() {
		String result[] = new String[mixerLocations.size()];
		for (int i = 0; i < result.length; i++) {
			result[i] = mixersNames.get(i);
		}
		return result;
	}

	//Esto devolvería las líneas para la interfaz. Pero todavía no chequeo si hay mixers con más de una línea...
	public String[] getLines() {
		String result[] = new String[4];
		for (int i = 0; i < result.length; i++) {
			result[i] = String.valueOf(i + 1);
		}
		return result;
	}

	//Acá configuramos e iniciamos las líneas requeridas...
	public void setConfig(int channels, int tMixer[], int tLines[]) {
		Mixer mixers[] = new Mixer[channels];
		nTest = channels;
		for (int i = 0; i < channels; i++) {
			try {
				mixers[i] = AudioSystem.getMixer(mixerInfo[mixerLocations.get(tMixer[i])]);
				Line.Info lInfo = mixers[i].getSourceLineInfo()[tLines[i]];
				lines[i] = (SourceDataLine) mixers[i].getLine(lInfo);
				lines[i].open(af, BUFFER_SIZE);
				lines[i].start();
				System.out.println("-- Línea configurada...");
			} catch (LineUnavailableException lue) {
				System.out.println("-- Ups, the line...");
				throw new RuntimeException(lue);
			} catch (Exception e) {
				System.out.println("-- Ups, unknown...");
				throw new RuntimeException(e);
			}
		}
	}

	//Acá reproducimos los archivos...
	public void play() {
		playing.set(true);
		new Thread(() -> {
			try {
				while (playing.get()) {
					for (int m = 0; m < nTest; m++) {
						streams[m].read(buffer);
						lines[m].write(buffer, 0, BUFFER_SIZE);
					}
				}
			} catch (Exception e) {
				System.out.println("Ups, the play...");
				System.out.println(e.toString());
				playing.set(false);
				throw new RuntimeException(e);
			}
		}).start();
	}

	public void stop() {
		playing.set(false);
	}

}
