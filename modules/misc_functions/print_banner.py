##################################################################
"""
Name  : print_banner.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable

def print_banner():

    print(fr"""
    {global_variable.GREEN}###############################################################################################################################
    {global_variable.GREEN}###############################################################################################################################
    {global_variable.GREEN}###                                                                                                                         ###
    {global_variable.GREEN}### {global_variable.YELLOW}██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░  {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.YELLOW}██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗  {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.YELLOW}██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝  {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.YELLOW}██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗  {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.YELLOW}██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║  {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.YELLOW}╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  {global_variable.GREEN}###
    {global_variable.GREEN}###                                                                                  {global_variable.YELLOW}by Net-Square(https://net-square.com)  {global_variable.GREEN}###
    {global_variable.GREEN}###                                                                                                                         {global_variable.GREEN}###
    {global_variable.GREEN}###                                                                                                                         {global_variable.GREEN}###
    {global_variable.GREEN}### 	               {global_variable.YELLOW}The First-Ever! Advance Browser Based Automated Web Form Fuzzing Tool                            {global_variable.GREEN}###
    {global_variable.GREEN}### 	               {global_variable.YELLOW}Version      : {global_variable.BLUE}v2025.4                                                                           {global_variable.GREEN}###
    {global_variable.GREEN}###                        {global_variable.YELLOW}Github       : {global_variable.BLUE}https://github.com/netsquare/BrowserBruter                                        {global_variable.GREEN}###
    {global_variable.GREEN}###                        {global_variable.YELLOW}Copyright    : {global_variable.BLUE}Net-Square Solutions PVT LTD. (https://net-square.com)                            {global_variable.GREEN}###
    {global_variable.GREEN}###                        {global_variable.YELLOW}Documentation: {global_variable.BLUE}https://net-square.com/browserbruter                                              {global_variable.GREEN}###
    {global_variable.GREEN}###                                                                                                                         {global_variable.GREEN}###
    {global_variable.GREEN}###        {global_variable.RED}     ..,:dOkxl:.                                                                                                 {global_variable.GREEN}###
    {global_variable.GREEN}###         {global_variable.RED}.,coooooooooooooc,.                                                                                             {global_variable.GREEN}###
    {global_variable.GREEN}###      {global_variable.RED}.,lllllllllllllllllllll,.                                                                                          {global_variable.GREEN}###
    {global_variable.GREEN}###     {global_variable.RED};ccccccccccccccccccccccccc;                                                                                         {global_variable.GREEN}###
    {global_variable.GREEN}###   {global_variable.RED}'ccccccccccccccccccccccccccccc.                                                                                       {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.GREEN} ,ooc::::::::ok{global_variable.RESET}O0000{global_variable.YELLOW}OOkkkkkkkkkkk:                _____                                                                 {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.GREEN}.ooool;;;;:x{global_variable.RESET}K0{global_variable.BLUE}kxxxxxk{global_variable.RESET}0X{global_variable.YELLOW}K0000000000.            .'{global_variable.RED}:::::::{global_variable.YELLOW}'.                                                              {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.GREEN}:oooool;,;O{global_variable.RESET}K{global_variable.BLUE}ddddddddddd{global_variable.RESET}KX{global_variable.YELLOW}000000000d       ___ /{global_variable.RED}:::::::::::{global_variable.YELLOW}\____ _            {global_variable.GREEN}_.''_                                      ###
    {global_variable.GREEN}### {global_variable.GREEN}lllllool;l{global_variable.RESET}N{global_variable.BLUE}dllllllllllld{global_variable.RESET}N{global_variable.YELLOW}K000000000    {global_variable.RESET}/{global_variable.YELLOW}||   ||`.______.-`||   | |\_{global_variable.BLUE}\\\\{global_variable.YELLOW}____/_{global_variable.GREEN} _.-'{global_variable.BLUE}\\\\{global_variable.RED}-- -- -- -- -- --                {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.GREEN}lllllllllo{global_variable.RESET}M{global_variable.BLUE}dccccccccccco{global_variable.RESET}W{global_variable.YELLOW}K000000000.{global_variable.RESET}|-|{global_variable.YELLOW} ||===||           ||===| ||_{global_variable.BLUE}||||{global_variable.YELLOW}____|_|{global_variable.GREEN} .-'{global_variable.BLUE}|||||{global_variable.RED}-- -- -- -- -- --               {global_variable.GREEN}###
    {global_variable.GREEN}### {global_variable.GREEN};cllllllllX{global_variable.RESET}X{global_variable.BLUE}c:::::::::c{global_variable.RESET}0X{global_variable.YELLOW}000000000d'{global_variable.RESET}|-|{global_variable.YELLOW} ||===||===========||===| ||_{global_variable.BLUE}||||{global_variable.YELLOW}____|_|{global_variable.GREEN}`-._{global_variable.BLUE}|||||{global_variable.RED}-- -- -- -- -- --               {global_variable.GREEN}###
    {global_variable.GREEN}### .ccccllllllO{global_variable.RESET}Nk{global_variable.BLUE}c;,,,;cx{global_variable.RESET}KK{global_variable.YELLOW}0000000000.    {global_variable.RESET}\{global_variable.YELLOW}||___||___________||___|_|/ {global_variable.BLUE}////{global_variable.YELLOW}   {global_variable.RESET}##{global_variable.GREEN}  `-._{global_variable.BLUE}////{global_variable.RED}-- -- -- -- -- --                {global_variable.GREEN}###
    {global_variable.GREEN}### .cccccclllllxOO{global_variable.RESET}OOOOkx{global_variable.YELLOW}O0000000000;          )  _____  (                     {global_variable.RESET}##                                           {global_variable.GREEN}###
    {global_variable.GREEN}###   {global_variable.GREEN}.:ccccccccllllllllo{global_variable.YELLOW}O0000000OOO,          / .'| {global_variable.RESET}({global_variable.YELLOW}  '. \                   {global_variable.RESET}##                                           {global_variable.GREEN}###
    {global_variable.GREEN}###     {global_variable.GREEN},:ccccccccclllcd{global_variable.YELLOW}0000OOOOOOl.          (  './    )   )                  {global_variable.RESET}##                                           {global_variable.GREEN}###
    {global_variable.GREEN}###       {global_variable.GREEN}'::ccccccccc{global_variable.YELLOW}dOOOOOOOkx:.             \ '._____.' /                   {global_variable.RESET}##                                           {global_variable.GREEN}###
    {global_variable.GREEN}###         {global_variable.GREEN}..,::cccc{global_variable.YELLOW}xOOOkkko;.                 '._______.'                    {global_variable.RESET}##                                           {global_variable.GREEN}###
    {global_variable.GREEN}###             {global_variable.GREEN}..,:{global_variable.YELLOW}dOkxl:.                                                    {global_variable.RESET}##                                           {global_variable.GREEN}###
    {global_variable.GREEN}###           {global_variable.RESET}###############                                                  {global_variable.RESET}##                                           {global_variable.GREEN}###
    {global_variable.GREEN}###          {global_variable.RESET}#################                                                {global_variable.RESET}####                                          {global_variable.GREEN}###
    {global_variable.GREEN}###         {global_variable.RESET}###################                                              {global_variable.RESET}######                                         {global_variable.GREEN}###
    {global_variable.GREEN}###############################################################################################################################
    {global_variable.GREEN}###############################################################################################################################{global_variable.RESET}""")
