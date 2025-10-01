#include <stdio.h>
#include <stdlib.h>

// declare structure to store block information (id, starting address, ending address, link to next block)

// declare linked list to connect allocation blocks
struct node{
    int id;
    int start_addr;
    int end_addr;
    struct node *link;
}*block_list = NULL;

typedef struct node block_type;

// declare global variables
int pm_size;
int hole_algo;
int remaining;

/********************************************************************/
void parameters() {
	// declare local variables (if any)

	// prompt for size of physical memory and choice of hole-fitting algorithm (0=first-fit, 1=best-fit), initialize remaining memory 
	printf("Enter size of physical memory: ");
	scanf("%d", &pm_size);
	printf("Enter hole fitting algorithm (0=first fit, 1=best_fit): " );
	scanf("%d", &hole_algo);
	
	//allocate memory for block list
	block_list = (block_type *)malloc(sizeof(block_type));

	// initilize linked list with "dummy" block of size 0
	block_list -> id = -1;
	block_list -> start_addr;
	block_list -> end_addr;
	block_list -> link = NULL;

	return;
}

/********************************************************************/
void print() {
	
	// declare local variables 
    block_type *current_block = block_list;
    //print header
    printf("\nID\tStart\tEnd\n");
    printf("--------------------\n");
    
	// print table containing block id, starting address, ending address
	while(current_block != NULL){
	    if(current_block->id != -1){
	        printf("%d\t%d\t%d\n",current_block->id, current_block->start_addr, current_block->end_addr);    
	    }
	    current_block = current_block->link;
	}

	return;
}

/********************************************************************/
void mem_alloc() {
	
	// declare local variables
    block_type *new_block, *current_block, *best_block;
    int new_id, new_size, hole_start, hole_end, hole_size, best_start, best_end;
    int at_least_one = 0;
	// initialize best hole so far to size of physical memory
	int best_hole = pm_size;
	remaining = pm_size;

	// prompt for block id & block size
	printf("Enter block id: ");
	scanf("%d", &new_id);
	
	printf("Enter block size: ");
	scanf("%d", &new_size);

	// check if size of block is larger than remaining unallocated space, if so, print message and return
	if (new_size > remaining){
	       printf("Not enough memory\n");
	       return;
	} // if not enough memory
    
	// allocate space for new block and set id
	new_block = (block_type *)malloc(sizeof(block_type));
	new_block -> id = new_id;
	
	// if only "dummy" block exists, insert block at end of linked list, set fields, return
	if (block_list -> link == NULL){
	    new_block -> start_addr = 0;
	    new_block -> end_addr = new_size;
	    new_block -> link = NULL;
	    block_list -> link = new_block;
	    print();
	    return;
	} // if only dummy block exists
	
	// else traverse list until either appropriate hole is found or the end of the list is reached
    current_block = block_list;
  
    while(current_block != NULL){
		// if id already exists, reject request and return
        if(new_id == current_block -> id){
            print("ID already exists in memory");
            return; 
        }
		// set values for start and end of currently found hole
		hole_start = current_block->end_addr;
        
		if(current_block -> link != NULL){
		    hole_end = current_block->link->start_addr;
		}
		else{
		    hole_end = pm_size;
		}
		hole_size = hole_end - hole_start;
		
		
		// if hole is large enough for block
		if(hole_size >= new_size){
		    at_least_one = 1;
		    
		    // if first-fit algorithm
		    if(hole_algo == 0){
				// set start & end fields of new block & add block into linked list
				new_block -> start_addr = current_block->end_addr;
				new_block -> end_addr = new_block -> start_addr + new_size;
				new_block -> link = current_block -> link;
				current_block -> link = new_block;
				// reduce remaining available memory and return
				remaining -= new_size;
			    print();
				return;
		    }
			// else--best-fit algorithm
			else{
			    // if hole is smaller than best so far
			   	if (hole_size < best_hole){
			   	    best_hole = hole_end - hole_start;
			   	    best_start = hole_start;
			   	    best_end = hole_end;
		    	    best_block = current_block;
		    	}
					// set values of best start & best end & best hole size so far
			}
		}
		// update best block & advance next block
		current_block = current_block -> link;
	}
	
	if(at_least_one==0){
	    printf("not enough memory available");
	    free(new_block);
	    return;
	}
	else{
	    new_block->start_addr=best_start;
	    new_block->end_addr=best_start + new_size;
	    new_block->link = best_block->link;
	    best_block ->link = new_block;
	    remaining -= new_block->end_addr - new_block-> start_addr;
	    print();
	}
			
		   
	// set start & end fields of new block & add block into linked list 	   
	
	// reduce remaining available memory and return
	
	return;	
}
	

/********************************************************************/
void mem_dealloc() {
    
	// declare local variables
	block_type *current_block, *prev_block; 
	int dealloc_id;
	
	// prompt for block id
    printf("Enter block id to deallocate: ");
    scanf("%d",&dealloc_id);
    
    current_block = block_list;
    
	// until end of linked list is reached or block id is found 
    while((current_block != NULL)&&(current_block->id != dealloc_id)){
        // traverse list
        prev_block = current_block;
	    current_block = current_block->link;    
	}
	
	// if end of linked list reached, print block id not found
	if (current_block == NULL){
	    printf("\nblock id not found\n");
	}
	// else remove block and deallocate memory
	else{
	    prev_block->link = current_block->link;
	    remaining += current_block->end_addr -current_block->start_addr;
	    free (current_block);
	    print();
	}

	return;
}


/********************************************************************/
void defrag() {
	// declare local variables 	   
    block_type *current_block = block_list; 
    int prev_end = 0;
    int block_size;
    
	// until end of list is reached
    while(current_block != NULL){
        // calculate current hole size
        block_size = current_block->end_addr - current_block->start_addr;
        
        // adjust start & end fields of current block to eliminate hole
        current_block->start_addr = prev_end;
        current_block->end_addr = current_block->start_addr + block_size;
        prev_end = current_block->end_addr;
        current_block = current_block->link;
    }
		
    print();    
	return;
}


/********************************************************************/
void garbage_collection(block_type *node) {
	// if node is NULL, return
    if (node == NULL){
        return;
    }
	// else
    else {
        //recursively call procedure on node->link
        garbage_collection(node->link);
        
        // deallocate memory from node
        free(node);
    }
	return;
}


/***************************************************************/
int main() {
    /* Declare local variables */ 
    int choice = 0;
    int p;
  
    /* Until the user quits, print the menu, prompt for the menu choice, call the appropriate procedure */ 
    while (choice != 5){
        printf ("\nMemory Allocation\n");
        printf ("---------------------\n");
        printf ("1) Enter parameters\n");
        printf ("2) Allocate memory for block\n");
        printf ("3) Deallocate memory for block\n");
        printf ("4) Defragment memory\n");
        printf ("5) Quit program\n");
      
        printf ("\nEnter selection: ");
        scanf ("%d", &choice);
      
        p++;
      
        switch (choice){
            case 1: parameters(); break;
	        case 2: mem_alloc(); break;
	        case 3: mem_dealloc(); break;
	        case 4: defrag(); break;
	        case 5: garbage_collection (block_list);
	            printf ("\nQuitting program\n"); break;
	        default:
	            printf ("Invalid option!\n"); break;
	   }/* switch statement */
    }/* while loop */

	 return 1; /* indicates success */
} /* end of procedure */



