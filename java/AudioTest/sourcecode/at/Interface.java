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
import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Insets;
import java.net.URL;

public class Interface implements ActionListener {

	AudioControl ac;

	Color black = new Color(35, 35, 35);
	Color red = new Color(190, 40, 40);
	Color green = new Color(0, 255, 95);

	JButton play = new JButton();

	JPanel panels[] = new JPanel[4];
	JComboBox mixers[] = new JComboBox[4];
	JComboBox channels[] = new JComboBox[4];

	Font frameFont;
	Font buttonsFont;

	public Interface (AudioControl audioControl){
		System.out.println("-- Iniciamos una prueba con audio");
		ac = audioControl;
		buildFrame();
	}

	/////////
	//Actions
	public void actionPerformed (ActionEvent ae) {

		if(ae.getSource() == play) {
			int m[] = new int[4];
			int l[] = new int[4];
			for (int i = 0; i < 4; i++) {
				m[i] = mixers[i].getSelectedIndex();
				l[i] = channels[i].getSelectedIndex();
			}
			try {
				ac.triggerPlay(m, l);
			} catch (Exception e) {
				fatalError();
			}
		}

	}

	////////////////////////////
	//Let's build the windown...
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

		for (int i = 0; i < panels.length; i++) {
				p.add(Box.createRigidArea(new Dimension (0, 10)));
				p.add(channelPanel(i, auxm, auxch));
		}
		p.add(Box.createRigidArea(new Dimension (0, 10)));
		p.add(buttonsPanel());
		p.add(Box.createRigidArea(new Dimension (0, 10)));
		p.add(classInfoPanel());
		p.add(Box.createRigidArea(new Dimension (0, 10)));

		return p;

	}

	JPanel channelPanel(int i, String[] mix, String[] ch){

		mixers[i] = new JComboBox(mix);
		channels[i] = new JComboBox(ch);

		JPanel p = new JPanel();
		p.setLayout(new BoxLayout(p, BoxLayout.X_AXIS));
		p.add(Box.createRigidArea(new Dimension (10, 0)));
		p.add(mixers[i]);
		p.add(Box.createRigidArea(new Dimension (10, 0)));
		p.add(channels[i]);
		p.add(Box.createRigidArea(new Dimension (10, 0)));

		return p;

	}

	JPanel buttonsPanel(){

		JPanel p = new JPanel();
		p.setOpaque(true);
		p.setLayout(new BoxLayout(p, BoxLayout.X_AXIS));

		play.setText("play");
		play.setFont(buttonsFont);
		play.setVisible(true);
		play.addActionListener(this);

		Dimension d = new Dimension(25, 0);

		p.add(Box.createRigidArea(d));
		p.add(play);
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

	/////////////////
	// Error handling
	void fatalError(){
		JOptionPane.showMessageDialog(new JFrame(),
   				"Hubo un problemita...",
  				"Ups",
			JOptionPane.WARNING_MESSAGE);
	}

}
