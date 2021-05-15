package at;

import javax.swing.JComponent;
import javax.swing.Box;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.JComboBox;
import javax.swing.JOptionPane;
import javax.swing.JLabel;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Insets;
import java.net.URL;

public class Interface implements ActionListener {

	AudioControl ac;

	JButton play = new JButton();
	JButton stop = new JButton();
	JButton config = new JButton();

	JPanel panels[] = new JPanel[4];
	JComboBox channels = new JComboBox();
	JComboBox mixers[] = new JComboBox[4];
	JComboBox lines[] = new JComboBox[4];

	Font frameFont;
	Font buttonsFont;

	//Recibimos una objeto de tipo AudioControl por constructor...
	public Interface (AudioControl audioControl){
		ac = audioControl;
		buildFrame();
	}

	//Definimos qué hacen los botones...
	public void actionPerformed (ActionEvent ae) {

		if(ae.getSource() == config) {
			int c = channels.getSelectedIndex() + 1;
			int m[] = new int[4]; //Acá carcamos los valores de las JComboBox
			int l[] = new int[4];
			for (int i = 0; i < 4; i++) {
				m[i] = mixers[i].getSelectedIndex();
				l[i] = lines[i].getSelectedIndex();
			}
			try {
				ac.setConfig(c, m, l);
				successfulSet();
			} catch (Exception e) {
				fatalError();
			}
		} else if (ae.getSource() == play) {
			try {
				ac.play();
			} catch (Exception e) {
				fatalError();
			}
		} else if (ae.getSource() == stop) {
			ac.stop();
		}
	}

	//Construimos la ventana...
	void buildFrame() {

		JFrame v = new JFrame("Nuestra ventana");
		v.setDefaultCloseOperation(3);
		v.setResizable(true);

		frameFont = new Font("monospace", Font.PLAIN, 12);
		buttonsFont = new Font("monospace", Font.BOLD, 13);

		v.setSize(400, 300);
		v.setLocationRelativeTo(null);
		v.add(builPanel());
		v.setVisible(true);

	}

	//Building the frame's panels...
	JPanel builPanel(){

		JPanel p = new JPanel();
		p.setLayout(new BoxLayout(p, BoxLayout.Y_AXIS));

		String[] auxm = ac.getMixers();
		String[] auxch = ac.getLines();

		p.add(Box.createRigidArea(new Dimension (0, 10)));
		p.add(channelsPanel());

		for (int i = 0; i < panels.length; i++) {
				p.add(Box.createRigidArea(new Dimension (0, 10)));
				p.add(linesPanel(i, auxm, auxch));
		}
		p.add(Box.createRigidArea(new Dimension (0, 10)));
		p.add(buttonsPanel());
		p.add(Box.createRigidArea(new Dimension (0, 10)));
		p.add(classInfoPanel());
		p.add(Box.createRigidArea(new Dimension (0, 10)));

		return p;

	}

	JPanel channelsPanel(){

		JPanel p = new JPanel();

		JLabel channelsLabel = new JLabel("<html><div align='left'>Cantidad de canales:</div><html>", JLabel.CENTER);
		channelsLabel.setFont(frameFont);

		String c[] = {"1","2","3","4"};
		channels = new JComboBox(c);

		p.setLayout(new BoxLayout(p, BoxLayout.X_AXIS));
		p.add(Box.createRigidArea(new Dimension (10, 0)));
		p.add(channelsLabel);
		p.add(Box.createRigidArea(new Dimension (10, 0)));
		p.add(channels);
		p.add(Box.createRigidArea(new Dimension (10, 0)));


		return p;

	}

	JPanel linesPanel(int i, String[] mix, String[] l){

		mixers[i] = new JComboBox(mix);
		lines[i] = new JComboBox(l);

		JPanel p = new JPanel();
		p.setLayout(new BoxLayout(p, BoxLayout.X_AXIS));
		p.add(Box.createRigidArea(new Dimension (10, 0)));
		p.add(mixers[i]);
		p.add(Box.createRigidArea(new Dimension (10, 0)));
		p.add(lines[i]);
		p.add(Box.createRigidArea(new Dimension (10, 0)));

		return p;

	}

	JPanel buttonsPanel(){

		JPanel p = new JPanel();
		p.setOpaque(true);
		p.setLayout(new BoxLayout(p, BoxLayout.X_AXIS));

		config.setText("set");
		config.setFont(buttonsFont);
		config.setVisible(true);
		config.addActionListener(this);

		play.setText("play");
		play.setFont(buttonsFont);
		play.setVisible(true);
		play.addActionListener(this);

		stop.setText("stop");
		stop.setFont(buttonsFont);
		stop.setVisible(true);
		stop.addActionListener(this);


		Dimension d = new Dimension(25, 0);

		p.add(Box.createRigidArea(d));
		p.add(config);
		p.add(Box.createRigidArea(d));
		p.add(play);
		p.add(Box.createRigidArea(d));
		p.add(stop);
		p.add(Box.createRigidArea(d));

		p.setPreferredSize(new Dimension(650, 35));

		return p;

	}

	JPanel classInfoPanel(){

		JPanel p = new JPanel();
		p.setOpaque(true);
		p.setLayout(new BoxLayout(p, BoxLayout.X_AXIS));
		JLabel classInfo = new JLabel("<html><div align='center'>testing, testing, testing..."
									+ "<br>Algo va a salir.</div><html>", JLabel.CENTER);
		classInfo.setFont(frameFont);
		p.add(classInfo);

		return p;

	}

	//Errores y otros mensajes...
	void fatalError(){
		JOptionPane.showMessageDialog(new JFrame(),
   				"Hubo un problemita...",
  				"Ups",
			JOptionPane.ERROR_MESSAGE);
	}

	void successfulSet(){
		JOptionPane.showMessageDialog(new JFrame(),
   				"¡Esto es un éxito!",
  				"Ya estoy listo...",
			JOptionPane.INFORMATION_MESSAGE);
	}

}
