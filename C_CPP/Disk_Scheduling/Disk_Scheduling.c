#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Declare global variables, including dynamic array to store sequence of traversed tracks
int *sequence = NULL;
int sequence_size;

/*********************************************************/
void parameters () {
    
	// prompt for the sequence size
    printf("Enter size of sequence: ");
    scanf("%d", &sequence_size);
    
	// allocate memory for the sequence of traversed tracks
	sequence = (int *)malloc(sizeof(sequence_size));

	// prompt for starting track, store in index 0
    printf("Enter starting track: ");
    scanf("%d", &sequence[0]);
    
	// prompt for sequence of tracks to seek, store in index 1 to "sequence size-1"
    printf("Enter sequence of tracks to seek: ");
    for(int i = 1; i < sequence_size; i++){
        scanf("%d", &sequence[i]);
    }
	return;

} // "OPTION #1"


/*********************************************************/
void FIFO () {

	// declare local variables		
	int total_distance = sequence[0];
	
	printf("Traversed Sequence: %d", sequence[0]);
	
	// calculate total distance of traversed tracks
    for(int i = 1; i < sequence_size; i++){
		total_distance += abs(sequence[i] - sequence[i-1]);

		// print current index value of sequence
		printf(" %d", sequence[i]);
	}

	// print total distance of tracks traversed
    printf("\nThe distance of the traversed tracks is: %d\n", total_distance);
	return;

} // "OPTION #2"	


/*********************************************************/
void SSTF() {

	// declare local variables and initialize current track and distance traversed to starting track
    int total_distance = sequence[0];
    int current_track = sequence[0];
    int num_done = 1;
    int *done = (int*)calloc(sequence_size, sizeof(int));
    int shortest_index;
    
	// begin printing sequence of traversal 
    printf("Traversed Sequence: %d ", sequence[0]);
    
	// until every track is traversed
    while (num_done < sequence_size){
        // initilize shortest distance to INT_MAX
        int shortest_distance = INT_MAX;
        
        // for each track in sequence
        for(int i = 1; i < sequence_size; i++){ 
        
            // if not already traversed
            if(done[i]==0){
                
                //if distance to traverse is shorter than current shortest distance
                if((abs(sequence[i] - current_track)) < shortest_distance){
                    
                    // set current shortest distance and index of the track	w/ shortest distance 
                    shortest_distance = abs(sequence[i] - current_track);
                    shortest_index  = i;
                    
                }// end if
            }// end if
        }// end for
        
        // set "done" value for track w/shortest distance to 1 (mark as traversed)
        done[shortest_index] = 1;
        
        // increment number of tracks that have been traversed
        num_done++;
        
        // update total distance traversed
        total_distance += abs(sequence[shortest_index] - current_track);
        
        //set current track to new position, print position
        current_track = sequence[shortest_index];
        printf("%d ", current_track);
    }// end while

  	// print total distance traversed
  	printf("\nThe distance of the traversed tracks is: %d\n", total_distance);
	
	return;

} // "OPTION #3" 


/*********************************************************/
void SCAN() {

	// declare local variables
    int direction;
	int at_least_one;
	int total_distance = sequence[0];
    int current_track = sequence[0];
    int num_done = 1;
    int *done = (int*)calloc(sequence_size, sizeof(int));
    int shortest_index;
	
	//prompt for initial direction (0=descreasing, 1=increasing)
	printf("Enter initial direction: ");
    scanf("%d", &direction);
    
	// initialize current track and distance traversed to starting track
    //int total_distance = sequence[0];
	//int current_track = sequence[0];
	
	// begin printing sequence of traversal 
    printf("Traversed Sequence: %d ", sequence[0]);
    
	// until every track is traversed
    while (num_done < sequence_size){
        at_least_one = 0;
        
        // initilize shortest distance to INT_MAX
        int shortest_distance = INT_MAX;
        
        // for each track in sequence
        for(int i = 1; i < sequence_size; i++){ 
            // if not already traversed
            if(done[i]==0){
                //if distance to traverse is shorter than current shortest distance in the current direction
                if((abs(sequence[i] - current_track)) < shortest_distance){
				    if((((sequence[i] - current_track) > 0) && (direction ==1)) ||
					   (((sequence[i] - current_track) < 0) && (direction ==0))){
					        shortest_distance = abs(sequence[i] - current_track);
                            shortest_index  = i;
                            at_least_one = 1;
				    }// end if
                }// end if		   
            }// end if
        } // end for
        if(at_least_one==1){
            done[shortest_index] = 1;
            num_done++;
            total_distance += abs(sequence[shortest_index] - current_track);
            current_track = sequence[shortest_index];
            printf("%d ", current_track);
        }
        else{
            direction = 1 - direction;
        }
    }// end while
		
    printf("\nThe distance of the traversed tracks is: %d\n", total_distance);

	return;

} // "OPTION #4"


/*********************************************************/
void CSCAN() {

	// declare local variables
    int end_reached = 0;
	int at_least_one;
	int total_distance = sequence[0];
    int current_track = sequence[0];
    int num_done = 1;
    int *done = (int*)calloc(sequence_size, sizeof(int));
    int shortest_index;
    

	// begin printing sequence of traversal 
    printf("Traversed Sequence: %d ", sequence[0]);
    
	// until every track is traversed
    while (num_done < sequence_size){
        at_least_one = 0;
        
        // initilize shortest distance to INT_MAX
        int shortest_distance = INT_MAX; 
        
        // for each track in sequence
        for(int i = 1; i < sequence_size; i++){ 
            
            // if not already traversed
            if(done[i]==0){
                if(((sequence[i] - current_track) < shortest_distance) && (sequence[i] - current_track) > 0){
				    shortest_distance = sequence[i] - current_track;
                    shortest_index  = i;
                    at_least_one = 1;   
                }// end if
            }//end if
        }//end for
        if(at_least_one==1){
            done[shortest_index] = 1;
            num_done++;
            if(end_reached==1){
                current_track = sequence[shortest_index];
                total_distance -= shortest_distance;
                end_reached = 0;
                printf("%d ", current_track);
            }
            else{
                total_distance += abs(sequence[shortest_index] - current_track);
                current_track = sequence[shortest_index];
                printf("%d ", current_track);
            }
        }
        else{
            total_distance += current_track;
            current_track = 0;
            end_reached = 1;
        }
    }//end while
    
    printf("\nThe distance of the traversed tracks is: %d\n", total_distance);
	return;    

} // "OPTION #5


/***************************************************************/
void garbage_collection() {

	if (sequence != NULL)
		free(sequence);
	return;

} // "OPTION #6


/***************************************************************/
int main() {
    /* Declare local variables */ 
    int choice = 0;
    int p;
  
    /* Until the user quits, print the menu, prompt for the menu choice, call the appropriate procedure */ 
    while (choice != 6){
        printf ("\nMemory Allocation\n");
        printf ("---------------------\n");
        printf ("1) Enter parameters\n");
        printf ("2) Calculate distance to traverse tracks using FIFO\n");
        printf ("3) Calculate distance to traverse tracks using SSTF\n");
        printf ("4) Calculate distance to traverse tracks using Scan\n");
        printf ("5) Calculate distance to traverse tracks using C-Scan\n");
        printf ("6) Quit program and free memory\n");
      
        printf ("\nEnter selection: ");
        scanf ("%d", &choice);
      
        p++;
      
        switch (choice){
            case 1: parameters(); break;
	        case 2: FIFO(); break;
	        case 3: SSTF(); break;
	        case 4: SCAN(); break;
	        case 5: CSCAN(); break;
	        case 6: garbage_collection ();
	            printf ("\nQuitting program\n"); break;
	        default:
	            printf ("Invalid option!\n"); break;
	   }/* switch statement */
    }/* while loop */

	 return 1; /* indicates success */
} /* end of procedure */

