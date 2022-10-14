#include "lists.h"
#include <stdlib.h>
/**
 * 
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	temp = *head;
	while (temp)
	{
		if (temp->n > number)
		{
			new_node->next = temp;
			temp = new_node;
			return (new_node);
		}
		temp = temp->next;
	}
	return (NULL);
}
