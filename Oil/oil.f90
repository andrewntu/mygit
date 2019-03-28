Program start
integer::n,i
character(6),Allocatable::cdate(:),gmax(:),gmin(:),diff(:),avg(:),change(:)
open(1,file = '20002017.csv',status = 'old')
open(2,file = '20002017.txt',status = 'unknown')
n = 0
do i = 1,1
read(1,*)
enddo
do i = 1,5000
	read(1,*,err = 99)
	n = n+1
enddo
99 close(1)
Allocate(cdate(n))
Allocate(gmax(n))
Allocate(gmin(n))
Allocate(diff(n))
Allocate(avg(n))
Allocate(change(n))


open(1,file = '20002017.csv',status = 'old')
do i = 1,1
read(1,*)
enddo

do i = 1,n
	read(1,*,err=100)cdate(i),gmax(i),gmin(i),diff(i),avg(i),change(i)
	write(2,'(I4,1x,A6)')i,gmax(i)
enddo
100 close(1)
!print*,gmax
end
