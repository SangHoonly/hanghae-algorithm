/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode *odd = head;
        ListNode *even = head == nullptr? nullptr : head->next;
        ListNode *evenFirst = even;

        if (odd == nullptr || even == nullptr || even->next == nullptr) return head;


        while (odd->next != nullptr  && even->next != nullptr ) {

            if (odd->next == even) {
                odd->next = even->next;
                odd = even->next;
            } else {
                even->next = odd->next;
                even = odd->next;
            }
        };

        even->next = nullptr;
        odd->next = evenFirst;


        return head;
    }
};
