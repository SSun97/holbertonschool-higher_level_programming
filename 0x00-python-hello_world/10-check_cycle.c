#include "lists.h"
/**
 * check_cycle - check if there is a cycle on the list
 * @list: type listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p1 = list, *p2 = list;

	if (list)
	{
		while (p1 && p2)
		{
			p1 = p1->next;
			p2 = p2->next->next;
			if (p1 == p2)
				return (1);
		}
	}
	return (0);
}
