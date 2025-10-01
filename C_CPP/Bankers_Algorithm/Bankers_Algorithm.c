#include <stdio.h>
#include <stdlib.h>

/* Declare dynamic arrays and global variables*/ 
int *resource = NULL;
int *available = NULL;
int *max_claim = NULL;
int *allocated = NULL;
int *need = NULL;

int num_resources, num_processes;

/***********************************************************/ 
void print_resource_vector() {
    /* declare local variables */ 
    int i;
  
    printf ("\tUnits\tAvailable\n");
    for (i=0; i<num_resources; i++){
        printf("r%d\t%d\t%d\n", i, resource[i], available[i]);
    }
    printf("\n");
    /* for loop: print each resource index */ 
    /* for loop: print number of total units and available units of each resource index */ 
    return;
}
  
 
/***************************************************************/ 
void print_matrix() { 
  /* declare local variables */ 
  int i, j;

  /* for loop: print each resource index */
    printf ("\tMaximum");
    for(i=0; i<num_resources; i++){
        printf ("\t");
    }
    printf ("Current");
    for(i=0; i<num_resources; i++){
        printf ("\t");
    }
    printf ("Need\n");
    
    for(i=0; i<3; i++){
        for(j=0; j<num_resources; j++){
            printf ("\tr%d", j);    
        }
    }
    printf("\n");
    
    for(i=0; i<num_processes; i++){
        printf ("p%d\t", i);
        for (j=0; j<num_resources; j++){
            printf("%d\t", max_claim[i*num_resources+j]);
        }
        for (j=0; j<num_resources; j++){
            printf("%d\t", allocated[i*num_resources+j]);
        }
        for (j=0; j<num_resources; j++){
            printf("%d\t", need[i*num_resources+j]);
        }
        printf("\n");
    }
  /* for each process: */ 
  /* for each resource: */ 
  /* print maximum number of units each process may request, is allocated, and needs from each resource */ 
  return;
}
  
 
/****************************************************************/ 
void parameters (){
    /* declare local variables */ 
    int i, j;
    
    /* prompt for number of processes and number of resources */ 
    printf ("Enter number of processes: ");
    scanf ("%d", &num_processes);
    printf ("Enter number of resources: ");
    scanf ("%d", &num_resources);
  
    
    /* allocate memory for vectors and arrays: resource, available, max_claim, allocated, need */ 
    resource = malloc(num_resources* sizeof(int));
    available = malloc(num_resources* sizeof(int));
    max_claim = (int *) malloc(num_processes * num_resources* sizeof(int));
    allocated = (int *) malloc(num_processes * num_resources* sizeof(int));
    need = (int *) malloc(num_processes * num_resources* sizeof(int));
    
    /* for each resource, prompt for number of units, set resource and available vectors indices */ 
    printf ("Enter number of units for resources (r0 to r%d) : ", num_resources - 1);
    for (i=0; i<num_resources; i++){
        scanf ("%d", &resource[i]);
        available[i] = resource[i];
    }
    
    /* for each process, for each resource, prompt for maximum number of units requested by process, update max_claim and need arrays */
    for (i=0; i<num_processes; i++){
        printf ("Enter max units process p%d will request from each resource (r0 to r%d) : ", i, num_resources - 1);
        for(j=0; j<num_resources; j++){
            scanf("%d", &max_claim[i*num_resources+j]);
            need[i*num_resources+j] = max_claim[i*num_resources+j];
        }
    }
    
    /* for each process, for each resource, prompt for number of resource units allocated to process */ 
    for (i=0; i<num_processes; i++){
        printf ("Enter number of units of each resource (r0 to r%d) allocated to process p%d : ", num_resources - 1, i);
        for(j=0; j<num_resources; j++){
            scanf("%d", &allocated[i*num_resources+j]);
            need[i*num_resources+j] -= allocated[i*num_resources+j];
            available[j] -= allocated[i*num_resources+j];
        }
    }
    /* print resource vector, available vector, max_claim array, allocated array, need array */ 
    print_resource_vector();
    print_matrix();
    return;
}
/********************************************************************/ 
void sequence (){
    /* declare local variables, including vector to indicate if process is safely sequenced and "num_sequenced" count */
    int i, j;
    int less_than_or_equal, at_least_one = 1;
    int finished = 0;
    
    int *sequenced = (int*)calloc(num_processes, sizeof(int));
    
    /* while not all processed are sequenced */ 
    while((finished < num_processes) && (at_least_one == 1)){
        at_least_one = 0;
        /* for each process */
        for(i=0; i<num_processes; i++){
            if(sequenced[i] == 0){    
                //printing the fluff
                printf("Checking: < ");
                for(j=0; j<num_resources; j++){
                    printf("%d ", need[i*num_resources+j]);
                }
                
                printf("> <= < ");
                
                for(j=0; j<num_resources; j++){
                    printf("%d ", available[j]);
                }
                printf("> ");
                
                //check if resource is less than or equal
                less_than_or_equal = 1;
                for(j=0; j<num_resources; j++){
                    if ((available[j] < need[i*num_resources+j]) && (less_than_or_equal == 1)){
                        less_than_or_equal = 0;    
                    }
                }
                
                if (less_than_or_equal == 1){
                    printf(":p%d safely sequenced\n",i);
                    for(j=0; j<num_resources; j++){
                        available[j] += allocated[i*num_resources+j];
                    }
                    finished++;
                    sequenced[i] = 1;
                    at_least_one = 1;
                }
                else {
                    printf(":p%d could not be sequenced\n",i); 
                }
            }    
        }
        if (at_least_one == 0){
            printf("Deadlock");    
        }
    }            
    
    return;

}

/********************************************************************/ 
void garbage_collection (){
  
    /* check if vectors/array are not NULL--if so, free each vector/array */ 
    if(resource != NULL){
        free (resource);
        free (available);
        free(max_claim);
        free(allocated);
        free(need);
    }
  
return;

}

/***************************************************************/ 
int main(){
    /* Declare local variables */ 
    int choice = 0;
    int p;
  
    /* Until the user quits, print the menu, prompt for the menu choice, call the appropriate procedure */ 
    while (choice != 3){
        printf ("\nBanker's Algorithm\n");
        printf ("---------------------\n");
        printf ("1) Enter parameters\n");
        printf ("2) Determine safe sequence\n");
        printf ("3) Quit program\n");
      
        printf ("\nEnter selection: ");
        scanf ("%d", &choice);
      
        p++;
      
        switch (choice){
            case 1: parameters(); break;
	        case 2: sequence(); break;
	        case 3: garbage_collection ();
	            printf ("\nQuitting program\n"); break;
	        default:
	            printf ("Invalid option!\n"); break;
	   }/* switch statement */
    }/* while loop */
    
return 1;
}

