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
        void AddNode(ListNode **tail, ListNode **l)
        {
                ListNode *newNode = new ListNode((*l)->val);
                (*tail)->next = newNode;
                *tail = newNode;
                *l = (*l)->next;
        }

        ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {

            ListNode *head = new ListNode();
            ListNode *tail = head;

            while (l1 != nullptr && l2 != nullptr) {
                if (l1->val > l2->val) AddNode(&tail, &l2);
                else AddNode(&tail, &l1);
            };

            while (l1 != nullptr) AddNode(&tail, &l1);
            while (l2 != nullptr) AddNode(&tail, &l2);

            return head->next;
        }
};
