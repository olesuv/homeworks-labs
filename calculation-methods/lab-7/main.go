package main

import (
	"fmt"
	"math"
	"math/rand"
	"os"
)

func main() {
	matrix_A, err := os.Create("matrix_A.txt")
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer matrix_A.Close()

	n := 100
	a, b := 1.0, 9.0

	for i := 1; i <= n; i++ {
		for j := 1; j < n; j++ {
			r_numb := a + b*float64(rand.Intn(1000000000))/1000000000.0
			fmt.Fprintf(matrix_A, "%f\t", r_numb)
		}
		r_numb := a + b*float64(rand.Intn(1000000000))/1000000000.0
		fmt.Fprintf(matrix_A, "%f\n", r_numb)
	}
}

func normalVector(x []float64) float64{
  max := 0.0

  for _, v := range x {
    if math.Abs(v) > max {
      max = math.Abs(v)
    }
  }

  return max
}

func LUFind(L, U, A [][]float64, n int){
	for k := 1; k <= n; k++{
		for i := k; i <= n; i++{
			sum := 0.0

			for j := 1; j <= k-1; j++{
				sum += L[i][j] * U[j][k]
			}
			L[i][k] = A[i][k] - sum
		}
		for i := k+1; i <= n; i++{
			sum := 0.0

			for j := 1; j <= k - 1; j++{
				for j := 1; j <= k-1; j++{
					sum += L[k][j] * U[j][i]
				}
				U[k][i] = (A[k][i] - sum) / L[k][k]
			}
		}
	}
}

func LUSolve(L, U [][]float64, B, X []float64, n int){
	Z := make([]float64, n+1)
	sum, k, j := 0.0, 0.0, 0.0

	Z[1] = B[1] / L[1][1]

	for k = 2; k <= n; k++{
		sum := 0.0

		for j := 1; j <= k-1; j++{
			sum += L[k][j] * Z[j]
		}
		Z[k] = (B[k] - sum) / L[k][k]
	}
}
