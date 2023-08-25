#include "lists.h"

/**
 * check_cycle - uses Floyd's cycle detection algorithm to check
 *		for a circle in a linked list
 * @list: Pointer to the head of the linked list
 * Return: 0 if no cycle, 1 if a cycle is detected
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		/* move one step */
		slow = slow->next;
		/* move 2 steps */
		fast = fast->next->next;

		/* if thy colide, there is a cycle */
		if (slow == fast)
			return (1);
	}

	/* no cycle found in list */
	return (0);
}
