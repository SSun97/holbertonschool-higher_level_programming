#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: type listint_t **
 * @n: int n
 * Return: position of new added node.
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
	*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > n)
			{
				new->next = current->next;
				current->next = new;
				break;
			}
			current = current->next;
		}
		current->next = new;
	}

	return (new);


}
