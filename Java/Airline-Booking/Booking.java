import java.util.ArrayList;
import javax.swing.JOptionPane;

public class Booking{
	public static void main(String[] args){
		ArrayList<String> a = new ArrayList<String>();
		a.add("0");
		a.add("1");
		a.add("2");
		a.add(" ");
		a.add("4");
		a.add("5");
		a.add("6");
		ArrayList<String> b = new ArrayList<String>();
		b.add("0");
		b.add("1");
		b.add("2");
		b.add(" ");
		b.add("4");
		b.add("5");
		b.add("6");
		ArrayList<String> c = new ArrayList<String>();
		c.add("0");
		c.add("1");
		c.add("2");
		c.add(" ");
		c.add("4");
		c.add("5");
		c.add("6");
		ArrayList<String> d = new ArrayList<String>();
		d.add("0");
		d.add("1");
		d.add("2");
		d.add(" ");
		d.add("4");
		d.add("5");
		d.add("6");
		ArrayList<String> e = new ArrayList<String>();
		e.add("0");
		e.add("1");
		e.add("2");
		e.add(" ");
		e.add("4");
		e.add("5");
		e.add("6");
		ArrayList<String> f = new ArrayList<String>();
		f.add("0");
		f.add("1");
		f.add("2");
		f.add(" ");
		f.add("4");
		f.add("5");
		f.add("6");
		int theTimes=0;
		String u;
		u=JOptionPane.showInputDialog("Amount of seats to book:");
		int amount=Integer.parseInt(u);
		while(theTimes<amount){
			System.out.println("A "+a);
			System.out.println("B "+b);
			System.out.println("C "+c);
			System.out.println("D "+d);
			System.out.println("E "+e);
			System.out.println("F "+f);
			String s;
			s=JOptionPane.showInputDialog("Enter the row letter (LOWER CASE ONLY):");
		//String row=String.parseString(s);
			System.out.println("Row: "+s+".");
			String t;
			t=JOptionPane.showInputDialog("Enter the seat number:");
			int seat=Integer.parseInt(t);
			System.out.println("Row: "+s+" seat: "+seat+".");
			switch(s){
				case "a":
				a.remove(seat);
				System.out.println("Booked Row A, Seat "+seat);
				a.add(seat,"X");
				break;
				case "b":
				b.remove(seat);
				System.out.println("Booked Row B, Seat "+seat);
				b.add(seat,"X");
				break;
				case "c":
				c.remove(seat);
				System.out.println("Booked Row C, Seat "+seat);
				c.add(seat,"X");
				break;
				case "d":
				d.remove(seat);
				System.out.println("Booked Row A, Seat "+seat);
				d.add(seat,"X");
				break;
				case "e":
				e.remove(seat);
				System.out.println("Booked Row B, Seat "+seat);
				e.add(seat,"X");
				break;
				case "f":
				f.remove(seat);
				System.out.println("Booked Row C, Seat "+seat);
				f.add(seat,"X");
				break;
				default:
				System.out.println("ERROR");

			}
			theTimes+=1;
		}
			System.out.println("A "+a);
			System.out.println("B "+b);
			System.out.println("C "+c);
			System.out.println("D "+d);
			System.out.println("E "+e);
			System.out.println("F "+f);
		
	}
}