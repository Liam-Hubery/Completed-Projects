import javax.swing.JOptionPane;

public class TrapeziumCalculator{
	public static void main(String[] args) {
		
		String t;
		t=JOptionPane.showInputDialog("Enter one parallel side:");
		double y = Double.parseDouble(t);
		
		String s;
		s=JOptionPane.showInputDialog("Enter the other parallel side:");
		double x = Double.parseDouble(s);
		
		String u;
		u=JOptionPane.showInputDialog("Enter the height:");
		double z = Double.parseDouble(u);
		
		calculator.trapezium(x, y, z);
	}
}
class writing{
	public static void number(int f) {
		System.out.println(f);
	}
	public static void decimal(double g) {
		System.out.println(g);
	}
}
class calculator{
	public static void trapezium(double a, double b, double height) {
		double area=((a+b)*height)/2;
		JOptionPane.showMessageDialog(null, area, "Area", JOptionPane.INFORMATION_MESSAGE);
	}
}
		
