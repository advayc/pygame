# Main Function
```mermaid
flowchart TD
    main(Main Function) --> loading_screen
```
# Loading Screen Function
```mermaid
flowchart TD
    loading_screen(Loading Screen) -->|Gradually increase x of car image| check_end{Check if car_rect.right >= screen_width}
    check_end -->|Yes| welcome
    check_end -->|No| loading_screen
```
# Welcome Screen Function
```mermaid
flowchart TD
    welcome(Welcome Screen) --> decision{Click on button}
    decision -->|Start| roadmap
    decision -->|Instructions| instructions
```
# Instructions Function
```mermaid
flowchart TD
    instructions(Instructions) --> read_file[Read instructions.txt file]
    read_file --> display_instructions[Blit instructions on screen]
    display_instructions --> go_back_button[Go back button]
    go_back_button --> decision{Click on button}
    decision -->|Go Back| welcome
```
# Roadmap Screen Function
```mermaid
flowchart TD
    roadmap(Roadmap Screen) --> decision{Current count}
    decision -->|1| evone
    decision -->|2| evtwo
    decision -->|3| evthree
    decision -->|4| evfour
    decision -->|5| evfive
    decision -->|6| evsix
```
# evone Function
```mermaid
flowchart TD
    evone(Evone) --> blit_track1[Blit track1 img]
    blit_track1 --> blit_car[Blit car img at start of track]
    blit_car --> check_position{Car at first ev station}
    check_position -->|Yes| activity_1
    check_position -->|No| evone
```
# evtwo Function
```mermaid
flowchart TD
    evtwo(Evtwo) --> blit_track1[Blit track1 img]
    blit_track1 --> blit_car[Blit car img at second ev station]
    blit_car --> check_position{Car at second ev station}
    check_position -->|Yes| activity_2
    check_position -->|No| evtwo
```
# evthree Function
```mermaid
flowchart TD
    evthree(Evthree) --> blit_track2[Blit track2 img]
    blit_track2 --> blit_car[Blit car img at start of track]
    blit_car --> check_position{Car at first ev station}
    check_position -->|Yes| activity_3
    check_position -->|No| evthree
```
# evfour Function
```mermaid
flowchart TD
    evfour(Evfour) --> blit_track2[Blit track2 img]
    blit_track2 --> blit_car[Blit car img at second ev station]
    blit_car --> check_position{Car at second ev station}
    check_position -->|Yes| activity_4
    check_position -->|No| evfour
```
# evfive Function
```mermaid
flowchart TD
    evfive(Evfive) --> blit_track3[Blit track3 img]
    blit_track3 --> blit_car[Blit car img at start of track]
    blit_car --> check_position{Car at first ev station}
    check_position -->|Yes| activity_5
    check_position -->|No| evfive
```
# evsix Function
```mermaid
flowchart TD
    evsix(Evsix) --> blit_track3[Blit track3 img]
    blit_track3 --> blit_car[Blit car img at second ev station]
    blit_car --> check_position{Car at second ev station}
    check_position -->|Yes| activity_6
    check_position -->|No| evsix
```
# activity_1 Function

```mermaid
flowchart TD
    activity_1(Activity 1) --> display_activity1[Display activity 1]
    display_activity1 --> check_answer{Correct answer?}
    check_answer -->|Yes| congratulations_1[Congratulations screen]
    check_answer -->|No| retry_1[Retry screen]
    congratulations_1 --> roadmap
    retry_1 --> activity_1
```
# activity_2 Function

```mermaid
flowchart TD
    activity_2(Activity 2) --> display_activity2[Display activity 2]
    display_activity2 --> check_answer{Correct answer?}
    check_answer -->|Yes| congratulations_2[Congratulations screen]
    check_answer -->|No| retry_2[Retry screen]
    congratulations_2 --> roadmap
    retry_2 --> activity_2
```
# activity_3 Function

```mermaid
flowchart TD
    activity_3(Activity 3) --> display_activity3[Display activity 3]
    display_activity3 --> check_answer{Correct answer?}
    check_answer -->|Yes| congratulations_3[Congratulations screen]
    check_answer -->|No| retry_3[Retry screen]
    congratulations_3 --> roadmap
    retry_3 --> activity_3
```
# activity_4 Function

```mermaid
flowchart TD
    activity_4(Activity 4) --> display_activity4[Display activity 4]
    display_activity4 --> check_answer{Correct answer?}
    check_answer -->|Yes| congratulations_4[Congratulations screen]
    check_answer -->|No| retry_4[Retry screen]
    congratulations_4 --> roadmap
    retry_4 --> activity_4
```
# activity_5 Function

```mermaid
flowchart TD
    activity_5(Activity 5) --> display_activity5[Display activity 5]
    display_activity5 --> check_answer{Correct answer?}
    check_answer -->|Yes| congratulations_5[Congratulations screen]
    check_answer -->|No| retry_5[Retry screen]
    congratulations_5 --> roadmap
    retry_5 --> activity_5
```
# activity_6 Function

```mermaid
flowchart TD
    activity_6(Activity 6) --> display_activity6[Display activity 6]
    display_activity6 --> check_answer{Correct answer?}
    check_answer -->|Yes| finish_screen
    check_answer -->|No| retry_6[Retry screen]
    finish_screen --> congratulations[Congratulations screen]
    retry_6 --> activity_6
  ```  
# Finish Screen Function

```mermaid
flowchart TD
    finish_screen(Finish Screen) --> display_finish[Display final screen]
    display_finish --> play_again_button[Play again button]
    play_again_button --> decision{Click on button}
    decision -->|Yes| reset_game
```
# Reset Game Function
```mermaid
flowchart TD
    reset_game(Reset Game) --> reset_variables[Reset game variables]
    reset_variables --> welcome
```
