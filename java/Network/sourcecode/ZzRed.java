import java.io.IOException;
import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.net.SocketException;
import java.net.InetAddress;

public class ZzRed {

	public static void main (String[] args) {
		try {
			DatagramSocket dS = new DatagramSocket(9876);
			String m = "Esto es un mensaje";
			byte[] buffer = m.getBytes();
			DatagramPacket dP = new DatagramPacket(buffer, buffer.length, InetAddress.getLocalHost(), 8765);
			dP.setPort(8765);
			dS.send(dP);
		} catch (SocketException ese) {
			System.out.println("Ups");
		} catch (IOException eio) {
			System.out.println("Ups");
		}
	}

}
