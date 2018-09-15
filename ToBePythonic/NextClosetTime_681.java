package google;

import java.awt.geom.AffineTransform;
import java.text.Format;
import java.util.HashSet;
import java.util.Set;

public class NextClosetTime_681 {
	// Solution 1: time simulation
	public String nextClosestTime_1(String time) {
		//change string to number
		int cur = Integer.parseInt(time.substring(0,2))*60;
		cur += Integer.parseInt(time.substring(3));
		
		Set<Integer> allowed = new HashSet();
		for (char c : time.toCharArray()) 
			if (c!=':') {
				allowed.add(c-'0');
			}
		while (true) {
			// counting by minutes
			cur = (cur+1)%(60*24);
			int[] digits = new int[] {cur/60/10,cur/60%10,cur%60/10,cur%60%10};
			
			search:{
				for (int d: digits) 
					if (!allowed.contains(d))
						break search;
				return String.format("%02d:%02d",cur/60,cur%60);
			}
			
		}
		
	}
	
	//Solution2: Build from allowed digit

	public String nextClosestTime(String time) {
		int start = 60*Integer.parseInt(time.substring(0,2));
		start += Integer.parseInt(time.substring(3));
		
		int ans = start;
		int maxElapsed = 24*60;
		
		Set<Integer> allowed = new HashSet<>();
		
		for(char c:time.toCharArray())
			if (c!=':') {
				allowed.add(c-'0');
			}
		
		for (int h1:allowed) for(int h2:allowed) if(h1*10+h2<24) {
			for(int m1:allowed) for(int m2:allowed) if(m1*10+m2<60) {
				int cur = 60*(h1*10+h2)+(m1*10+m2);
				int candElapsed = Math.floorMod(cur-start, 24*60);
				if (0<candElapsed && candElapsed < maxElapsed) {
					ans  = cur;
					maxElapsed = candElapsed;
				}
			}
		}
		
		return String.format("%02d:%02d", ans/60,ans%60);
			
		
	}
	
	public static void main(String[] argvs) {
		NextClosetTime_681 time_681 = new NextClosetTime_681();
		String res=time_681.nextClosestTime("19:34");
		System.out.print(res);
	}

}
