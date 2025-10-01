#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

/* declare global variables including a table structure to hold scheduling information */
int num_processes;
//struct node first[num_processes];

struct node {
    int id;
    int arrival;
    int total;
    int done;
    int start_time;
    int end_time;
    int turnaround_time;
    int total_remaining;
    int already_started;
}*table = NULL; /* pointer */
typedef struct node table_type;

/* optional: define a function that finds the maximum of two integers */
#define max(a,b) (a > b ? a : b)
/***************************************************************/
void print_process() {
	
	/* declare local variables */
    int i;
	/* print table header */
	printf("\nID\tArrival\tTotal\tStart\tEnd\tTurnaround\n");
	printf("--------------------------------------------------\n");
	
	/* for each process */
	for (i=1; i<=num_processes;i++){
	    
	    /* print the contents (id, arrival time, total_cycles) of each field of the table's index */
	    printf("%d\t%d\t%d\t", table[i].id, table[i].arrival, table[i].total);
	    
	    /* if process has been scheduled ("done" field is 1, print other contents (start time, end time, turnaround time) */
	    if(table[i].done == 1){
	        printf("%d\t%d\t%d\n", table[i].start_time, table[i].end_time, table[i].turnaround_time);
	    }
	    else{
	        printf("\n");
	    }
	};
	
	return;
}


/***************************************************************/
void parameters() {
	
	/* declare local variables */
    int i;
    
	/* prompt for total number of processes */
	printf("Enter total number of processes: ");
	scanf("%d", &num_processes);
    
    /* allocate memory for table to hold process parameters */
	table = (table_type*)malloc(num_processes*sizeof(table_type));
	
	/* for each process */
	for (i=1; i<=num_processes;i++){
	    
	    /* prompt for process id, arrival time, and total cycle time */	
	    printf("Enter process id: ");
	    scanf("%d", &table[i].id);
	    printf("Enter arrival cycle for process P[%d]: ", table[i].id);
	    scanf("%d", &table[i].arrival);
	    printf("Enter total cycle for process P[%d]: ", table[i].id);
	    scanf("%d", &table[i].total);
	}; /* end for loop */ 
	
	/* print contents of table */
    print_process();
    
	return;		
}	
		

/***************************************************************/
void FIFO() {

	/* declare (and initilize when appropriate) local variables */
    int i;
    int j = 0;
    int min_val;
    int min_index;
    int cycle_time = 0;
    
	/* for each process, reset "done" field to 0 */
    for (i=1; i<=num_processes; i++){
        table[i].done = 0;
    }; /* end for */
    
	/* while there are still processes to schedule */
	while (j < num_processes){
	    /* initilize the earliest arrival time to INT_MAX (largest integer value) */
	    min_val = INT_MAX;
	    
	    /* for each process not yet scheduled */
	    for (i=1; i<=num_processes; i++){
            if(table[i].done==0){
                
                /* check if process has earlier arrival time than current earliest and update */
                if(table[i].arrival < min_val){
                    min_val = table[i].arrival;
                    min_index = i;
                } /* end if */
            } /* end if */
        }; /* end for */
        
        /* set start time, end time, turnaround time, done fields for unscheduled process with earliest arrival time */  
        table[min_index].start_time = max(cycle_time, table[min_index].arrival);
        table[min_index].end_time = table[min_index].start_time + table[min_index].total;
        table[min_index].turnaround_time = table[min_index].end_time - table[min_index].arrival; 
        table[min_index].done = 1;
        
        /* update current cycle time and increment number of processes scheduled */
        cycle_time = table[min_index].end_time;
	    j++;
	}; /* end while */

	/* print contents of table */
	print_process();
	
	return;		
}	


/***************************************************************/
void SJF() {
    /* declare (and initilize when appropriate) local variables */
    int i;
    int j = 0;
    int min_val;
    int min_index;
    int cycle_time = 0;
    
	/* for each process, reset "done" field to 0 */
    for (i=1; i<=num_processes; i++){
        table[i].done = 0;
    }; /* end for */
	/* while there are still processes to schedule */
	while (j < num_processes){
	    
		/* initilize the lowest total cycle time to INT_MAX (largest integer value) */
        min_val = INT_MAX;
        
		/* for each process not yet scheduled */
		for (i=1; i<=num_processes; i++){
		    if(table[i].done==0){
                
                /* check if process has lower total cycle time than current lowest and has arrival time less than current cycle time and update */
                if((table[i].total < min_val) && (table[i].arrival <= cycle_time)){
                    min_val = table[i].total;
                    min_index = i;
                } /* end if */
            } /* end if */
		};
		
		/* set start time, end time, turnaround time, done fields for unscheduled process with lowest (and available) total cycle time */       	
        table[min_index].start_time = max(cycle_time, table[min_index].arrival);
        table[min_index].end_time = table[min_index].start_time + table[min_index].total;
        table[min_index].turnaround_time = table[min_index].end_time - table[min_index].arrival; 
        table[min_index].done = 1;
        
		/* update current cycle time and increment number of processes scheduled */
	    cycle_time = table[min_index].end_time;
	    j++;
	}; /* end while */
	
	/* print contents of table */
    print_process();
    
	return;		
}	
        	

/***************************************************************/
void SRT() {

	/* declare (and initilize when appropriate) local variables */
	int i;
	int j = 0;
	int min_val;
	int min_index;
	int cycle_time = 0;

	/* for each process, reset "done", "total_remaining" and "already_started" fields to 0 */
    for (i=1; i<=num_processes; i++){
        table[i].done = 0;
        table[i].total_remaining = table[i].total;
        table[i].already_started = 0;
        

    }; /* end for */
    
	/* while there are still processes to schedule */
	while (j < num_processes){
	    
	    /* initilize the lowest total remaining time to INT_MAX (largest integer value) */
	    min_val = INT_MAX;
	    
	    /* for each process not yet scheduled */
	    for (i=1; i<=num_processes; i++){
	        if(table[i].done == 0){
	            
	           /* check if process has lower total remaining time than current lowest and has arrival time less than current cycle time and update */	
	           if ((table[i].total_remaining < min_val) && (table[i].arrival <= cycle_time)){
	                min_val = table[i].total_remaining;
                    min_index = i;
	           } /* end if */
	        } /* end if */
	    }; /* end for */
	
	    /* set end time, turnaround time of process with lowest (and available) total remaining cycle time */
	    
	    if(table[min_index].already_started == 0) {   	
			table[min_index].start_time = max(cycle_time, table[min_index].arrival);
			table[min_index].end_time = table[min_index].start_time + (cycle_time + 1);
			table[min_index].turnaround_time = table[min_index].end_time - table[min_index].arrival;
			table[min_index].already_started = 1;
		
		} /* end if */
		
		else {
			table[min_index].end_time=table[min_index].start_time + (cycle_time + 1);
			table[min_index].turnaround_time = table[min_index].end_time - table[min_index].arrival;
	
		} /* end esle */
		
		table[min_index].total_remaining--; 
		cycle_time++;
		if(table[min_index].total_remaining == 0){
		    table[min_index].done = 1;
		    table[min_index].end_time = cycle_time;
		    table[min_index].turnaround_time = table[min_index].end_time - table[min_index].arrival;
		    j++;
		} /* end if */
	}; /* end while */

	/* print contents of table */
    print_process();
	return;		
}	
        	

/***************************************************************/
void garbage() {

	/* free the schedule table if not NULL */
	if (table != NULL){
		free(table);
	}

	return;
}


/***************************************************************/
int main() {
    /* declare local vars */
	int choice = 0;
    
    /* while user has not chosen to quit */
	while (choice != 5) {
	    
    	/* print menu of options */
    	printf("\nBatch scheduling\n");
    	printf("--------------------------------\n");
    	printf("1) Enter parameters\n");
    	printf("2) Schedule processes with FIFO algorithm\n");
    	printf("3) Schedule processes with SJF algorithm\n");
    	printf("4) Schedule processes with SRT algorithm\n");
    	printf("5) Quit and free memory\n");
        
        /* prompt for menu selection */
    	printf("\nEnter selection: ");
    	scanf("%d", &choice);
    	
	/* call appropriate procedure based on choice--using switch statement */
	switch(choice) {
		case 1: parameters(); break;
		case 2: FIFO(); break;
		case 3: SJF(); break;
		case 4: SRT(); break;
		case 5: garbage();
			printf("\nQuitting program...\n"); break;
		default: printf("Invalid \n"); break;
	} /* end switch statement */
} /* end while loop */

 return 1;
} /* end of procedure */








