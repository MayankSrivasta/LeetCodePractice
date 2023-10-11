package leetCode;

public class Catridge {

	public static boolean isPossible(int cartridges, int dollars, int recycleRewards, int perksCost,
			int noOdPerksToBuy) {
		int extra_dollars_needed = noOdPerksToBuy * perksCost - dollars;
		if (extra_dollars_needed > cartridges * recycleRewards)
			return false;
		if (extra_dollars_needed < 0)
			extra_dollars_needed = 0;

//		cartridges -= ((extra_dollars_needed / recycleRewards) + (extra_dollars_needed % recycleRewards != 0));

		return (cartridges >= noOdPerksToBuy) ? true : false;
	}

	public static int maxPerksItems(int cartridges, int dollars, int recycleReward, int perksCost) {

		int lo = 0, hi = Integer.MAX_VALUE;
		while (lo < hi) {
			int mid = (lo + hi + 1) / 2;
			if (!isPossible(cartridges, dollars, recycleReward, perksCost, mid))
				hi = mid - 1; // excluded region
			else
				lo = mid; // included region
		}
		return lo;
	}

}
