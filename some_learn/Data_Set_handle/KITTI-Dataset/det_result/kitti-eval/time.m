
tic;%tic1
t1=clock;
for i=1:3
    tic ;%tic2
    t2=clock;
    pause(3*rand)
    %计算到上一次遇到tic的时间，换句话说就是每次循环的时间
    disp(['toc计算第',num2str(i),'次循环运行时间：',num2str(toc)]);
    %计算每次循环的时间
    disp(['etime计算第',num2str(i),'次循环运行时间：',num2str(etime(clock,t2))]);
    %计算程序总共的运行时间
    disp(['etime计算程序从开始到现在运行的时间:',num2str(etime(clock,t1))]);
    disp('======================================')
end
%计算此时到tic2的时间，由于最后一次遇到tic是在for循环的i=3时，所以计算的是最后一次循环的时间
disp(['toc计算最后一次循环运行时间',num2str(toc)])
disp(['etime程序总运行时间：',num2str(etime(clock,t1))]);