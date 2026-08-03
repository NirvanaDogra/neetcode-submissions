class Solution {
    Stack<Integer> evalStack = new Stack<Integer>();
    public int evalRPN(String[] tokens) {
        for(String t: tokens) {
            switch(t) {
                case "+": {
                    int second = evalStack.pop();
                    int first = evalStack.pop();
                    evalStack.push(first+second);
                    break;
                }
                case "*": {
                    int second = evalStack.pop();
                    int first = evalStack.pop();
                    evalStack.push(first*second);
                    break;
                }
                case "-": {
                    int second = evalStack.pop();
                    int first = evalStack.pop();
                    evalStack.push(first-second);
                    break;
                }
                case "/": {
                    int second = evalStack.pop();
                    int first = evalStack.pop();
                    evalStack.push(first/second);
                    break;
                }
                default: {
                    evalStack.push(Integer.parseInt(t));
                    break;
                }
            }
        }
        return evalStack.peek();
    }
}
