import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;

class RandomizedSet {
    private List<Integer> nums;
    private HashMap<Integer, Integer> map;
    private Random rand;

    public RandomizedSet() {
        nums = new ArrayList<>();
        map = new HashMap<>();
        rand = new Random();
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (map.containsKey(val)) {
            return false;
        }
        nums.add(val);
        map.put(val, nums.size() - 1);
        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (!map.containsKey(val)) {
            return false;
        }
        int last = nums.get(nums.size() - 1);
        int index = map.get(val);
        nums.set(index, last);
        map.put(last, index);
        nums.remove(nums.size() - 1);
        map.remove(val);
        return true;
    }

    /** Get a random element from the set. */
    public int getRandom() {
        int randomIndex = rand.nextInt(nums.size());
        return nums.get(randomIndex);
    }
}

// Question: https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
