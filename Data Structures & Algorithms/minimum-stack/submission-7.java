class MinStack {
    record StackMeta(int val, int minTillNow){}
    private List<StackMeta> meta;

    public MinStack() {
        meta = new ArrayList<>();
    }
    
    public void push(int val) {
        if (meta.size() == 0) {
            meta.add(new StackMeta(val, val));
        } else {
            int previousMin = meta.get(meta.size() - 1).minTillNow;
            int minVal = Math.min(previousMin, val);
            meta.add(new StackMeta(val, minVal));
        }
        System.out.println(val+ " " +top());
    }
    
    public void pop() {
        meta.remove(meta.size() - 1);
    }
    
    public int top() {
        return meta.get(meta.size() - 1).val;
    }
    
    public int getMin() {
        return meta.get(meta.size() - 1).minTillNow;
    }
}
