class Solution:
    def calculate(self, s: str) -> int:
        def operation(m1, m2, op):
          if op == '+':
            return m1 + m2
          elif op == '-':
            return m1 - m2
          elif op=='*':
            return m1*m2
          elif op=='/':
            return m1//m2

        stack = []
        i = 0
        cur = None
        while i < len(s):
          if s[i].isdigit():
            j = i + 1
            num = [s[i]]
            while j < len(s) and s[j].isdigit():
              num.append(s[j])
              j += 1
            cur = int(''.join(num))
            i = j

          elif s[i] in '+-*/':
                stack.append(s[i])
                i += 1
          else:
            i += 1
          if cur != None:
            if not stack or stack[-1]=='+' or stack[-1]=='-':
              stack.append(cur)
            else:
              op = stack.pop()
              m1 = stack.pop()
              n = operation(m1, cur, op)
              stack.append(n)
            cur = None
        stack.reverse()
        while len(stack)>1:
          m1=stack.pop()
          op=stack.pop()
          m2=stack.pop()
          n = operation(m1, m2, op)
          stack.append(n)
        return stack[-1]