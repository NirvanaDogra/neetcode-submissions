class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack();
        String open = "({[";
        String close = ")}]";
        for(char ch: s.toCharArray()) {
            
            if(open.indexOf(ch)>-1) {
                stack.push(ch);
            } else {
                int index = close.indexOf(ch);
                if (!stack.isEmpty() && open.charAt(index) == stack.peek()) {
                    stack.pop();
                    
                } else {
                    return false;
                }
            }

            // stack.forEach(System.out::println);
        }

        return stack.isEmpty();
    }
}
