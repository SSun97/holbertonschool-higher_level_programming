#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - check if a linked list is palindrome
 * @head: double pointer of listint_t
 * Return: 1 if it is, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int values[10000];
	size_t a = 0, i, j;
	if (*head == NULL)
		return (0);
	while (*head != NULL)
	{
		values[a++] = (*head)->n;
		*head = (*head)->next;
	}
	for (i = 0, j = a - 1; i < j; ++i, --j)
	{
		if (values[i] != values[j])
			return (0);
	}

	return (1);
}
