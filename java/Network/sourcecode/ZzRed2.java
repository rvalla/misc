import java.io.IOException;
import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.net.SocketException;
import java.net.InetAddress;

public class ZzRed2 {

	public static void main (String[] args) {
		try {
			DatagramSocket dS = new DatagramSocket(8765);
			String m = "Esto es un mensaje";
			byte[] buffer = new byte[64];
			DatagramPacket dP = new DatagramPacket(buffer, buffer.length);
			dS.receive(dP);
			System.out.println(new String(buffer));
		} catch (SocketException ese) {
			System.out.println("Ups");
		} catch (IOException eio) {
			System.out.println("Ups");
		}
	}

}
