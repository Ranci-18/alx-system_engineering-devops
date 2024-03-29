#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 *infinite_while - function sleeps for 1 second after parent and
 *child process are created
 *
 *Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 *main - creates five zombie processes
 *
 *Return: always 0
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	infinite_while();
	return (0);
}
