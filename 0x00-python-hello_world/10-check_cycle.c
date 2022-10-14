#include "lists.h"
/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: the given list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	if (list == NULL)
		return (0);
	while (list->next && temp != list->next)
	{
		list = list->next;
	}
	if (temp == list->next)
		return (1);
	return (0);
}
