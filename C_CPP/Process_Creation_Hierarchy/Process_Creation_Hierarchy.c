#include <stdio.h>
#include <stdlib.h>

/* Define structures and global variables*/
int num_processes; 

/* linked list of children processes */

struct node1 {
	int process;
	struct node1 *link;
};

typedef struct node1 linked_list_type;

/* pcb structure */
struct node2 {
	int parent;
	linked_list_type *children;
} *pcb = NULL;

typedef struct node2 pcb_type;


/***************************************************************/
void print_processes() {
    
    /* delclare local variables */
	int i;
	linked_list_type *next;
	
	/* for each PCB index i from 0 up to (but not including) maximum number*/
	for (i=0; i<num_processes; i++) {
	    
	    /* check if PCB[i] has a parent and children */
		if ((pcb[i].parent !=-1) && (pcb[i].children != NULL)) {
		    
		    /* print message about children of the current PCB[i] */
			printf("PCB[%d] is the parent of: ",i);
			
			/* intilize variable to head of list of children */
			next = pcb[i].children;
			while (next != NULL) {
				printf("PCB[%d]  ",next->process);
				next=next->link;
			} /* end while */
			printf("\n");
		}	/* end if */
	} /* end for */
} /* end of procedure */

/***************************************************************/
void parameters() {
    /* declare local vars */
	int i;

    /* prompt for maximum number of processes */
	printf("Enter maximum number of processes: ");
	scanf("%d", &num_processes); 
	
	/* allocate memory for dynamic array of PCBs */
	pcb = (pcb_type *)malloc(num_processes * sizeof(pcb_type));

	/* Define PCB[0] */
	pcb[0].parent = 0;
	pcb[0].children = NULL;
	
	/* Intitialize all other indices' parent to -1 */
	for (i=1; i<num_processes; i++) {
		pcb[i].parent =-1;
	} /* end for-loop */

	return;

} /* end of procedure */

	
/***************************************************************/
void create() {
	
	/* define local vars */
	int p;
	int q = 0;
	linked_list_type *new_child, *next;
	int new_child_index = 1;	
	int num_child = 1;
	
	printf("Enter the parent process index: ");
	scanf("%d", &p);
	
	while (pcb[q].parent !=-1){
		q++;
	} /* while-loop */

	new_child = (linked_list_type *) malloc(sizeof(linked_list_type));
	new_child->process = q;
	new_child->link = NULL;

	/* record the parent's index p in PCB[q] */
	pcb[q].parent = p;

	/* initialize the list of children of PCB[q] as empty */
	pcb[q].children = NULL;

	/* create a new link containing the child's index q and appends the link to the linked list of PCB[p] */
	if(pcb[p].children==NULL) {
	   pcb[p].children = new_child;
   }
   else {
      next = pcb[p].children;
      num_child++;
		while (next->link!= NULL) {
			next = next->link;
			num_child++;
		} /* while-loop */

   next->link = new_child;
   }
   print_processes();
   
return;
} /* end of procedure */


/***************************************************************/
void delete_rec(linked_list_type *node) {
	/* declare local vars */
	int q;
	/* check if end of linked list--if so return */

	if (node ==  NULL) {
		return;
	} /* end if */
	
	/* else call self on next node in linked list */
	else {
		delete_rec(node->link);
		
		/* set variable q to current node's process index field */
		q = node->process;
		
		/* call self on children of PCB[q] */ 
		delete_rec(pcb[q].children);
		
		/* free memory of paramter */
		free(node);
		
		/* reset parent of PCB[q] to -1 */
		pcb[q].parent = -1;
		
		/* set paramter to NULL */
		node = NULL;
	} /* end of else */
return;
} /* end of procedure */


/***************************************************************/
void delete() {
    /* declare local vars */
	int p;
	
	/* prompt for process index p */
	printf("Enter the index of the process whose descendants are to be destroyed: ");
	scanf("%d", &p);
	
	/* call recursive procedure to destroy descendants of PCB[p] */
	delete_rec(pcb[p].children);
	
	/* reset children of PCB[p] to NULL */
	pcb[p].children	= NULL;	
	
	/* call procedure to print current hierarchy of processes */
	print_processes();
	return;
} /* end of procedure */


/***************************************************************/
void garbage() {
    /* check if PCB is non null */
	if (pcb != NULL) {
	    /* check if children of PCB[0] is not null */
	    if (pcb[0].children != NULL) {
	        printf("Free up memory... ");
	      
	        /* call recursive procedure to destroy children of PCB[0] */
		    delete_rec(pcb[0].children);
	    } /* end of if */
	   
	    /* free memory of PCB */
	    free(pcb);
	} /* end of if */
return;
} /* end of procedure */


/***************************************************************/
int main() {
    /* declare local vars */
	int choice = 0;
    
    /* while user has not chosen to quit */
	while (choice != 4) {
	    
    	/* print menu of options */
    	printf("\nProcess creation and destruction\n");
    	printf("--------------------------------\n");
    	printf("1) Enter parameters\n");
    	printf("2) Create a new child process\n");
    	printf("3) Destroy all descendants of a process\n");
    	printf("4) Quit program and free memory\n");
        
        /* prompt for menu selection */
    	printf("\nEnter selection: ");
    	scanf("%d", &choice);
    	
	/* call appropriate procedure based on choice--using switch statement */
	switch(choice) {
		case 1: parameters(); break;
		case 2: create(); break;
		case 3: delete(); break;
		case 4: garbage();
			printf("\nQuitting program...\n"); break;
		default: printf("Invalid \n"); break;
	} /* end switch statement */
} /* end while loop */

 return 1;
} /* end of procedure */

