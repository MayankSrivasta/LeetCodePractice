package leetCode;

public class CatridgeRecycling {

	

	int cartridges, dollars, recycleReward, perksCost;

	boolean isPossible(int cartridges, int dollars, int recycleRewards, int perksCost, int noOdPerksToBuy)
	{
		int extra_dollars_needed = noOdPerksToBuy*perksCost-dollars;
		if(extra_dollars_needed > cartridges*recycleReward)	
	        return false;
		if(extra_dollars_needed<0)  
	        extra_dollars_needed=0;

//		cartridges-=(extra_dollars_needed/recycleReward)+(extra_dollars_needed%recycleReward!=0);
		
		return (cartridges>=noOdPerksToBuy)	? true : false;
	}
	
	int  maxPerksItems(int cartridges, int dollars, int recycleReward, int perksCost) {

//		int lo = 0;
//		while (lo < hi) {
//			int mid = (lo + hi + 1) / 2;
//			if (!isPossible(cartridges, dollars, recycleReward, perksCost, mid))
//				hi = mid - 1; 
//			else
//				lo = mid; 
//		}
//		return lo;
		return 0;
	}
	
}
