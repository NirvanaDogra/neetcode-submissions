class MinStack {
    private Stack<Integer> stack = new Stack<>();
    private Stack<Integer> minStack = new Stack<>();
    private Integer minValue = Integer.MIN_VALUE;

    public MinStack() {
        
    }
    
    public void push(int val) {
        if(minStack.isEmpty()) {
            stack.push(val);
            minStack.push(val);
        } else {
            minValue = Math.min(minStack.peek(), val);
            minStack.push(minValue);
            stack.push(val);
        }
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
